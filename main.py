from fastapi import FastAPI,HTTPException,Path,Query,status,Depends
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBearer
from fastapi.security.http import HTTPAuthorizationCredentials
from pydantic import BaseModel,Field
from typing import List, Optional
from jwt_manager import create_token,validate_token

from starlette.requests import Request



notes = [
    {
        'id':1,
        'title':'My first note',
        'content':'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
    },
    {
        'id':2,
        'title':'My second note',
        'content':'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
    }
]

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        
        if data['email'] != "platziuser@fake.com":
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Ivalid Credentials")
        

class User(BaseModel):
    email:str
    password:str
    
    class Config:
        json_schema_extra = {
            "example":{
                'emal':'jhon.doe@example.com',
                'password':'123'
            }
        }

class Note(BaseModel):
    id:int = Field(le=2000)
    title:str = Field(min_length=5,max_length=15)
    content:str = Field(min_length=5,max_length=200)
    
    class Config:
        json_schema_extra = {
            "example":{
                'id':1,
                'title':'my title',
                'content':'my content'
            }
        }

app = FastAPI()

app.title = "Platzi project"

app.version = "0.0.1"

@app.post('/login',tags=['Auth'],status_code=status.HTTP_200_OK)
def login(user:User):
    if user.email == "platziuser@fake.com" and user.password == "admin123@":
        token:str = create_token(user.dict())
        return JSONResponse(status_code=status.HTTP_200_OK,content=token)
    return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED,content={"message":"Unauthorized"})
    
@app.get('/',tags=['Notes'],response_model=List[Note],status_code=status.HTTP_200_OK)
def get_notes() -> List[Note]:
    return JSONResponse(status_code=status.HTTP_200_OK,content=notes)

@app.get('/notes/{id}',tags=['Notes'],response_model=Note,status_code=status.HTTP_200_OK)
def get_note(id:int = Path(le=2000)) ->Note :
    note = [item for item in notes if item['id'] == id]
    
    if len(note) > 0 :
        return JSONResponse(status_code=status.HTTP_200_OK,content=note)
    
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,content=note)

@app.post('/notes',tags=['Notes'],response_model=dict,status_code=status.HTTP_200_OK,dependencies=[Depends(JWTBearer())])
def create_note(note:Note) -> dict:
    notes.append(note)
    return JSONResponse(status_code=status.HTTP_201_CREATED,content={"message":"Note created successfully"})

@app.put('/notes',tags=['Notes'],response_model=dict,status_code=status.HTTP_200_OK,dependencies=[Depends(JWTBearer())])
def update_note(id:int,note:Note)->dict:
    for item in notes:
        if item['id'] == id:
            item['title'] = note.title
            item['content'] = note.content
        return JSONResponse(status_code=status.HTTP_200_OK,content={"message":"Note updated successfully"})
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,content={"message":"Oops, something went wrong! Try again later."})

@app.delete('/notes/{id}',tags=['Notes'],response_model=dict,status_code=status.HTTP_200_OK,dependencies=[Depends(JWTBearer())])
def delete_note(id:int) -> dict:
    for item in notes:
        if item['id'] == id:
            notes.remove(item)
            return JSONResponse(status_code=status.HTTP_200_OK,content={"message":"Note deleted successfully"})
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,content={"message":"Oops, something went wrong! Try again later."})