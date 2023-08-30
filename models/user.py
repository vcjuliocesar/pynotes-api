from config.database import base as BaseModel
from sqlalchemy import Integer,String,Column,Boolean

class User(BaseModel):
    __tablename__ = "users"
    
    id = Column(Integer,primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)