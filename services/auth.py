from passlib.context import CryptContext

class Auth():
    def __init__(self):
        self.pwd_context = CryptContext(schemes=['bcrypt'],deprecated="auto")
        
    def verify_password(self,password:str,hash:str):
        return self.pwd_context.verify(password,hash)
    
    def get_password(self,password:str):
        return self.pwd_context.hash(password)