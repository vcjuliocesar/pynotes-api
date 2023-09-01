from pydantic import BaseModel,Field
from typing import Optional

class NoteBase(BaseModel):
    #id:Optional[int] = Field(default=None)
    title:str = Field(min_length=5,max_length=15)
    content:str = Field(min_length=5,max_length=200)
    
    class Config:
        json_schema_extra = {
            "example":{
                'title':'my title',
                'content':'my content'
            }
        }
class NoteCreate(NoteBase):
    pass

class Note(NoteBase):
    id:Optional[int] = Field(default=None)
    owner_id:int
    
    class Config:
        orm_mode:True