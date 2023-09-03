from config.database import Base
from sqlalchemy import Integer,String,Column,Boolean
from sqlalchemy.orm import relationship

class User(Base):
    
    __tablename__ = "users"
    
    id = Column(Integer,primary_key=True)
    
    email = Column(String,unique=True)
    
    password = Column(String)
    
    is_active = Column(Boolean,default=True)
    
    notes = relationship("Note",back_populates="owner")