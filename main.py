from fastapi import FastAPI,HTTPException,status
from fastapi.security import HTTPBearer
from utils.jwt_manager import validate_token
from starlette.requests import Request
from config.database import engine,Base
from middlewares.error_handler import ErrorHandler
from config.config import ProductionConfig,DevelopmentConfig
from utils.settings import Settings
from routers.note import note_router
from routers.user import user_router

settings = Settings()

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
        
app = FastAPI()

app.title = "Platzi project"

app.version = "0.0.1"

if settings.ENVIROMENT == "production":
    app.config = ProductionConfig
else:
    app.config = DevelopmentConfig

app.add_middleware(ErrorHandler)

app.include_router(user_router)

app.include_router(note_router)


Base.metadata.create_all(bind=engine)


    