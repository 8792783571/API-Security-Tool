from fastapi import FastAPI, Request
from gateway.middleware import SecurityMiddleware

print("***** MY APP.PY LOADED *****")

app = FastAPI(
    title="API Security Tool",
    version="1.0"
)

app.add_middleware(SecurityMiddleware)

@app.get("/")
def home():
    return {"message": "API Security Tool Running"}

@app.get("/test")
def test():
    return {"status": "working"}

from pydantic import BaseModel

class LoginRequest(BaseModel):
    username: str
    password: str

@app.post("/login")
async def login(data: LoginRequest):
    return {
        "status": "success",
        "received": data.dict()
    }

@app.get("/users")
def users():
    return {"users": ["Alice", "Bob", "Charlie"]}
