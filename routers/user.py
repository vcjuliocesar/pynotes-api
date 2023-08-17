from fastapi import status,APIRouter
from fastapi.responses import JSONResponse
from utils.jwt_manager import create_token
from schemas.user import User

user_router = APIRouter()

@user_router.post('/login',tags=['Auth'],status_code=status.HTTP_200_OK)
def login(user:User):
    if user.email == "platziuser@fake.com" and user.password == "admin123@":
        token:str = create_token(user.dict())
        return JSONResponse(status_code=status.HTTP_200_OK,content=token)
    return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED,content={"message":"Unauthorized"})