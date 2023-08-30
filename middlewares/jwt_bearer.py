from fastapi import HTTPException,status
from fastapi.security import HTTPBearer
from utils.jwt_manager import validate_token
from starlette.requests import Request
from services.user import UserService
from config.database import Session
from datetime import datetime,timedelta

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Ivalid Credentials")
        db = Session()
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        expire = datetime.fromtimestamp(data['exp'])
        user = UserService(db).get_user_by_email(email=data["email"])
        
        if not user:
            raise credentials_exception
        
        if expire is None:
            raise credentials_exception
        
        if datetime.utcnow() > expire:
            raise credentials_exception