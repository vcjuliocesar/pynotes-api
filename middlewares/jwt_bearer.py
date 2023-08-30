from fastapi import HTTPException,status
from fastapi.security import HTTPBearer
from utils.jwt_manager import validate_token
from starlette.requests import Request
from services.user import UserService
from config.database import Session

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        db = Session()
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        result = UserService(db).get_user_by_email(email=data["email"])
        
        if not result:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Ivalid Credentials")