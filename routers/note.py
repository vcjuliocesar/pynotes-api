from fastapi import Path,status,Depends,APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List
from config.database import Session
from middlewares.jwt_bearer import JWTBearer
from schemas.note import Note
from services.note import NoteService

note_router = APIRouter()

@note_router.get('/',tags=['Notes'],response_model=List[Note],status_code=status.HTTP_200_OK)
def get_notes() -> List[Note]:
    db = Session()
    result = NoteService(db).get_notes()
    if not result:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,content={"message":"Note not found"})
    
    return JSONResponse(status_code=status.HTTP_200_OK,content=jsonable_encoder(result))

@note_router.get('/notes/{id}',tags=['Notes'],response_model=Note,status_code=status.HTTP_200_OK)
def get_note(id:int = Path(le=2000)) ->Note :
    db = Session()
    result = NoteService(db).get_note(id)
    
    if not result:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,content={"message":"Note not found"})
    
    return JSONResponse(status_code=status.HTTP_200_OK,content=jsonable_encoder(result))
    
    

@note_router.post('/notes',tags=['Notes'],response_model=dict,status_code=status.HTTP_200_OK,dependencies=[Depends(JWTBearer())])
def create_note(note:Note) -> dict:
    db = Session()
    NoteService(db).create_note(note)
    return JSONResponse(status_code=status.HTTP_201_CREATED,content={"message":"Note created successfully"})

@note_router.put('/notes',tags=['Notes'],response_model=dict,status_code=status.HTTP_200_OK,dependencies=[Depends(JWTBearer())])
def update_note(id:int,note:Note)->dict:
    db = Session()
    result = NoteService(db).get_note(id)
    
    if not result:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,content={"message":"Oops, something went wrong! Try again later."})
    NoteService(db).update_note(id,note)
    return JSONResponse(status_code=status.HTTP_200_OK,content={"message":"Note updated successfully"})
    

@note_router.delete('/notes/{id}',tags=['Notes'],response_model=dict,status_code=status.HTTP_200_OK,dependencies=[Depends(JWTBearer())])
def delete_note(id:int) -> dict:
    db = Session()
    result = NoteService(db).get_note(id)
    if not result:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,content={"message":"Oops, something went wrong! Try again later."})
    NoteService(db).delete_note(id)
    return JSONResponse(status_code=status.HTTP_200_OK,content={"message":"Note deleted successfully"})