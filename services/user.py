from models.user import User as UserModel
from schemas.user import User,UserBase,UserCreate

class UserService():
    
    def __init__(self,db) -> None:
        self.db = db
        
    def get_user(self,id:int):
        return self.db.query(UserModel).filter(UserModel.id == id).first()
    
    def get_user_by_email(self,email:str):
        return self.db.query(UserModel).filter(UserModel.email == email).first()
    
    def create_user(self,user:UserCreate):
        print(user)
        return
        #hashed_password = ""
        #new_user = UserModel() 
        