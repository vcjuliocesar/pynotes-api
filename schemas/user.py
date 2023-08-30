from pydantic import BaseModel,Field
from typing import Optional


class UserBase(BaseModel):
    email:str
    class Config:
        json_schema_extra = {
            "example":{
                'email':'jhon.doe@fake.com',
                'password':'admin123@'
            }
        }

class UserCreate(UserBase):
    password:str = Field(min_length=8,max_length=16)
        
    
class User(UserBase):
    id:Optional[int] = Field(default=None)
    is_active:bool
    
    class Config:
       orm_mode = True