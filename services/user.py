from models.user import User as UserModel
from schemas.user import User,UserBase,UserCreate
from passlib.context import CryptContext

class UserService():
    
    def __init__(self,db) -> None:
        self.db = db
        self.pwd_context = CryptContext(schemes=['bcrypt'],deprecated="auto")
    
    def verify_password(self,password:str,hash:str):
        return self.pwd_context.verify(password,hash)
    
    def get_password(self,password:str):
        return self.pwd_context.hash(password) 

    def get_user(self,id:int):
        return self.db.query(UserModel).filter(UserModel.id == id).first()
    
    def get_user_by_email(self,email:str):
        return self.db.query(UserModel).filter(UserModel.email == email).first()
    
    def create_user(self,user:UserCreate):
        print(self.get_password(user.password))
        
        return
        #hashed_password = ""
        #new_user = UserModel() 
        