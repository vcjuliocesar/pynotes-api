from config.database import Base
from sqlalchemy import Integer,String,Column

class User(Base):
    
    __tablename__ = "users"
    
    id = Column(Integer,primary_key=True)
    email = Column(String)
    password = Column(String)