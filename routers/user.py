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
    check_user_exists(user)

    UserService(db).create_user(user)

    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "User created"})


def check_user_exists(user):
    if UserService(db).get_user_by_email(email=user.email):
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message": "User already exists"})


@user_router.post('/login', tags=['Auth'], status_code=status.HTTP_200_OK)
def login(user: UserCreate):
    validate_password(user)

    token: str = create_token(user.dict())

    return JSONResponse(status_code=status.HTTP_200_OK, content=token)


def validate_password(user):
    user_found = UserService(db).get_user_by_email(email=user.email)

    if not (user_found and Auth().verify_password(user.password, user_found.password)):
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content={"message": "Unauthorized"})
