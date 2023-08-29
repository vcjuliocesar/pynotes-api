from pydantic import BaseModel,Field
from typing import Optional

class User(BaseModel):
    id:Optional[int] = Field(default=None)
    email:str
    password:str = Field(min_length=8)
    
    class Config:
        json_schema_extra = {
            "example":{
                'email':'jhon.doe@example.com',
                'password':'mypassword123'
            }
        }