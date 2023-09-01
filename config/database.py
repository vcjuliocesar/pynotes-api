import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from utils.settings import Settings
from config.config import ProductionConfig,DevelopmentConfig

settings = Settings()

if settings.ENVIROMENT == "production":
    conf = ProductionConfig
    #database_url = f"postgresql://{settings.DB_USER}:{settings.DB_PASS}@{settings.DB_HOST}/{settings.DB_NAME}"
    database_url = conf.DATABASE_URI

else:
    conf = DevelopmentConfig
    
    #sqlite_file_name = "../database.sqlite"

    #base_dir = os.path.dirname(os.path.realpath(__file__))

    #database_url = f"sqlite:///{os.path.join(base_dir,sqlite_file_name)}"
    database_url = conf.DATABASE_URI

engine = create_engine(database_url,echo=True)

Session = sessionmaker(bind=engine)

Base = declarative_base() 