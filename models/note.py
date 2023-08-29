from config.database import base
from sqlalchemy import Column,Integer,String

class Note(base):
    
    __tablename__ = "notes"
    
    id = Column(Integer,primary_key=True)
    title = Column(String)
    content = Column(String)