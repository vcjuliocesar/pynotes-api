from config.database import Base
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship

class Note(Base):
    
    __tablename__ = "notes"
    
    id = Column(Integer,primary_key=True)
    
    title = Column(String)
    
    content = Column(String)
    
    owner_id = Column(Integer,ForeignKey("users.id"))
    
    owner = relationship("User",back_populates="notes") 