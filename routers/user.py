from fastapi import status,APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field
from typing import Optional
from jwt_manager import create_token

class User(BaseModel):
    id:Optional[int] = Field(default=None)
    email:str
    password:str
    
    class Config:
        json_schema_extra = {
            "example":{
                'email':'jhon.doe@example.com',
                'password':'123'
            }
        }

user_router = APIRouter()

@user_router.post('/login',tags=['Auth'],status_code=status.HTTP_200_OK)
def login(user:User):
    if user.email == "platziuser@fake.com" and user.password == "admin123@":
        token:str = create_token(user.dict())
        return JSONResponse(status_code=status.HTTP_200_OK,content=token)
    return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED,content={"message":"Unauthorized"})