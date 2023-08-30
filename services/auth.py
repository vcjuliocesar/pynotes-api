from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'],deprecated="auto")

def verify_password(password:str,hash:str):
    return pwd_context.verify(password,hash)

def get_password(password:str):
    return pwd_context.hash(password) 