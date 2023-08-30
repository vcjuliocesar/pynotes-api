from pydantic import BaseModel,Field
from typing import Optional


class UserBase(BaseModel):
    email:str

class UserCreate(UserBase):
    password:str
    
class User(UserBase):
    id:Optional[int] = Field(default=None)
    name:str
    is_active:bool
    
    class Config:
       orm_mode = True