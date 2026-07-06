# from starlette.middleware.base import BaseHTTPMiddleware

# class SecurityMiddleware(BaseHTTPMiddleware):
#     async def dispatch(self, request, call_next):
#         response = await call_next(request)
#         response.headers["X-Content-Type-Options"] = "nosniff"
#         response.headers["X-Frame-Options"] = "DENY"
#         return response


from urllib.parse import unquote
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.responses import JSONResponse

from scanner.sqli import detect_sqli
from scanner.xss import detect_xss
from scanner.traversal import detect_traversal


class SecurityMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):

        # Skip Swagger Docs
        path = request.url.path

        if path.startswith("/docs") or \
           path.startswith("/openapi.json") or \
           path.startswith("/redoc"):
            return await call_next(request)

        # Decode URL
        url = unquote(str(request.url))

        print("Scanning:", url)

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

        response = await call_next(request)

        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"

        return response
