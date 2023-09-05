from fastapi import status, APIRouter
from fastapi.responses import JSONResponse
from utils.jwt_manager import create_token
from schemas.user import User, UserBase, UserCreate
from config.database import Session
from services.user import UserService
from services.auth import Auth

user_router = APIRouter()
db = Session()


@user_router.post('/users', tags=['Auth'], response_model=User, status_code=status.HTTP_200_OK)
def create_user(user: UserCreate):
    if check_user_exists(user):
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message": "User already exists"})

    UserService(db).create_user(user)

    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "User created"})


def check_user_exists(user):
    return bool(UserService(db).get_user_by_email(email=user.email))


@user_router.post('/login', tags=['Auth'], status_code=status.HTTP_200_OK)
def login(user: UserCreate):

    if validates_password(user):
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content={"message": "Unauthorized"})

    token: str = create_token(user.dict())

    return JSONResponse(status_code=status.HTTP_200_OK, content=token)


def validates_password(user):
    user_found = UserService(db).get_user_by_email(email=user.email)

    return not bool(check_user_exists(user) and Auth().verify_password(user.password, user_found.password))
