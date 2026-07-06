from urllib.parse import unquote

from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.responses import JSONResponse

from scanner.sqli import detect_sqli
from scanner.xss import detect_xss
from scanner.traversal import detect_traversal
from scanner.jwt import validate_token
from scanner.rate_limit import allow_request
from scanner.headers import check_headers


class SecurityMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):

        ip = request.client.host

        # Rate Limiting
        if not allow_request(ip):
            return JSONResponse(
                {"error": "Rate Limit Exceeded"},
                status_code=429
            )

        # Decode URL
        url = unquote(str(request.url))

        # SQL Injection
        if detect_sqli(url):
            return JSONResponse(
                {"error": "SQL Injection Detected"},
                status_code=403
            )

        # XSS
        if detect_xss(url):
            return JSONResponse(
                {"error": "XSS Detected"},
                status_code=403
            )

        # Path Traversal
        if detect_traversal(url):
            return JSONResponse(
                {"error": "Path Traversal Detected"},
                status_code=403
            )

        # JWT Validation
        token = request.headers.get("Authorization")

        if token:
            if not validate_token(token):
                return JSONResponse(
                    {"error": "Invalid JWT"},
                    status_code=401
                )

        response = await call_next(request)

        check_headers(response)

        return response
