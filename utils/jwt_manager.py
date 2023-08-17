import os
from jwt import encode,decode
from dotenv import load_dotenv

load_dotenv()

def create_token(data:dict) -> dict:
    token:str = encode(payload=data,key=os.getenv('MY_SECRET_KEY'),algorithm="HS256")
    return token

def validate_token(token:str) -> dict:
    data:dict = decode(token,key=os.getenv('MY_SECRET_KEY'),algorithms=["HS256"]) 
    return data