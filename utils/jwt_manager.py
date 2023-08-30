import os
from jwt import encode,decode
from datetime import datetime,timedelta
from dotenv import load_dotenv

load_dotenv()

def create_token(data:dict) -> dict:
    payload = expire_token(data)
    token:str = encode(payload,key=os.getenv('MY_SECRET_KEY'),algorithm="HS256")
    return token

def validate_token(token:str) -> dict:
    data:dict = decode(token,key=os.getenv('MY_SECRET_KEY'),algorithms=["HS256"]) 
    return data

def expire_token(data:dict):
    to_encode = data.copy()
    token_expires = timedelta(minutes=int(os.getenv('TOKEN_EXPIRE_MINUTES')))
    expire = datetime.utcnow() + token_expires
    to_encode.update({'exp':expire})
    return to_encode