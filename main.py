from fastapi import FastAPI
from config.database import engine,base
from middlewares.error_handler import ErrorHandler
from routers.note import note_router
from routers.user import user_router


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

app.add_middleware(ErrorHandler)

app.include_router(user_router)

app.include_router(note_router)

base.metadata.create_all(bind=engine)



    