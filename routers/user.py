from fastapi import status,APIRouter
from fastapi.responses import JSONResponse
from utils.jwt_manager import create_token
from schemas.user import User
from config.database import session
from services.user import UserService
from services.auth import verify_password,get_password

user_router = APIRouter()



@user_router.post('/login',tags=['Auth'],status_code=status.HTTP_200_OK)
def login(user:User) -> str:
    db = session()
    data = UserService(db).find_user_by_email(user.email)
    if data and verify_password(user.password,data.password):
        token:str = create_token(user.dict())
        return JSONResponse(status_code=status.HTTP_200_OK,content=token)
    return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED,content={"message":"Unauthorized"})

# @user_router.put('/logout/{id}',tags=['Auth'],status_code=status.HTTP_200_OK)
# def logout(id):
#    pass
    
@user_router.post('/register',tags=['Auth'],status_code=status.HTTP_200_OK)
def register(user:User) -> dict:
    db = session()
    result = UserService(db).find_user_by_email(user.email)
    if not result:
        user.password = get_password(user.password)
        UserService(db).create_user(user)
        return JSONResponse(status_code=status.HTTP_200_OK,content={"message":"User created successfully"})
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,content={"message":"User already exists"})

# @user_router.put('/update',tags=['Auth'],status_code=status.HTTP_200_OK)
# def update(id:int,user:User):
#    pass

# @user_router.delete('/delete/{id}',tags=['Auth'],status_code=status.HTTP_200_OK)
# def logout(id:int):
#    pass