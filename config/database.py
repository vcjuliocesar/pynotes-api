import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from utils.settings import Settings
from config.config import ProductionConfig,DevelopmentConfig

settings = Settings()

if settings.ENVIROMENT == "production":
    conf = ProductionConfig
    
    database_url = conf.DATABASE_URI

else:
    conf = DevelopmentConfig
    
    database_url = conf.DATABASE_URI
    
engine = create_engine(database_url,echo=True)

Session = sessionmaker(bind=engine)

Base = declarative_base() 