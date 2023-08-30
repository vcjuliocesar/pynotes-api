from fastapi import status,APIRouter
from fastapi.responses import JSONResponse
from utils.jwt_manager import create_token
from schemas.user import User,UserBase,UserCreate
from config.database import Session
from services.user import UserService
from services.auth import Auth

user_router = APIRouter()

@user_router.post('/users',tags=['Auth'],response_model=User,status_code=status.HTTP_200_OK)
def create_user(user:UserCreate):
    db = Session()
    result = UserService(db).get_user_by_email(email=user.email)
    
    if not result:
        UserService(db).create_user(user)
        return JSONResponse(status_code=status.HTTP_200_OK,content={"message":"User created"})
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,content={"message":"User already exists"})

@user_router.post('/login',tags=['Auth'],status_code=status.HTTP_200_OK)
def login(user:UserCreate):
    db = Session()
    result = UserService(db).get_user_by_email(email=user.email)
    
    if result and Auth().verify_password(user.password,result.password):
        token:str = create_token(user.dict())
        return JSONResponse(status_code=status.HTTP_200_OK,content=token)
    return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED,content={"message":"Unauthorized"})