from fastapi import FastAPI,HTTPException,Path,status,Depends,APIRouter
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBearer
from fastapi.security.http import HTTPAuthorizationCredentials
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel,Field
from typing import List, Optional
from jwt_manager import create_token,validate_token
from starlette.requests import Request
from config.database import engine,Base,Session
from models.note import Note as NoteModel
from middlewares.jwt_bearer import JWTBearer


class Note(BaseModel):
    id:Optional[int] = Field(default=None)
    title:str = Field(min_length=5,max_length=15)
    content:str = Field(min_length=5,max_length=200)
    
    class Config:
        json_schema_extra = {
            "example":{
                'title':'my title',
                'content':'my content'
            }
        }

note_router = APIRouter()

@note_router.get('/',tags=['Notes'],response_model=List[Note],status_code=status.HTTP_200_OK)
def get_notes() -> List[Note]:
    db = Session()
    result = db.query(NoteModel).all()
    if not result:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,content={"message":"Note not found"})
    
    return JSONResponse(status_code=status.HTTP_200_OK,content=jsonable_encoder(result))

@note_router.get('/notes/{id}',tags=['Notes'],response_model=Note,status_code=status.HTTP_200_OK)
def get_note(id:int = Path(le=2000)) ->Note :
    db = Session()
    result = db.query(NoteModel).filter(NoteModel.id == id).first()
    
    if not result:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,content={"message":"Note not found"})
    
    return JSONResponse(status_code=status.HTTP_200_OK,content=jsonable_encoder(result))
    
    

@note_router.post('/notes',tags=['Notes'],response_model=dict,status_code=status.HTTP_200_OK,dependencies=[Depends(JWTBearer())])
def create_note(note:Note) -> dict:
    db = Session()
    new_note = NoteModel(**note.dict())
    db.add(new_note)
    db.commit()
    return JSONResponse(status_code=status.HTTP_201_CREATED,content={"message":"Note created successfully"})

@note_router.put('/notes',tags=['Notes'],response_model=dict,status_code=status.HTTP_200_OK,dependencies=[Depends(JWTBearer())])
def update_note(id:int,note:Note)->dict:
    db = Session()
    result = db.query(NoteModel).filter(NoteModel.id == id).first()
    
    if not result:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,content={"message":"Oops, something went wrong! Try again later."})
    result.title = note.title
    result.content = note.content
    db.commit()
    return JSONResponse(status_code=status.HTTP_200_OK,content={"message":"Note updated successfully"})
    

@note_router.delete('/notes/{id}',tags=['Notes'],response_model=dict,status_code=status.HTTP_200_OK,dependencies=[Depends(JWTBearer())])
def delete_note(id:int) -> dict:
    db = Session()
    result = db.query(NoteModel).filter(NoteModel.id == id).first()
    if not result:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,content={"message":"Oops, something went wrong! Try again later."})
    db.delete(result)
    db.commit()
    return JSONResponse(status_code=status.HTTP_200_OK,content={"message":"Note deleted successfully"})