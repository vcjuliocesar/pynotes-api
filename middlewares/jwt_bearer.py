from fastapi import HTTPException,status
from fastapi.security import HTTPBearer
from utils.jwt_manager import validate_token
from starlette.requests import Request


class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        
        if data['email'] != "platziuser@fake.com":
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Ivalid Credentials")