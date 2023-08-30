from models.user import User as UserModel
from schemas.user import User,UserBase,UserCreate
from services.auth import Auth

class UserService():
    
    def __init__(self,db) -> None:
        self.db = db
        
    def get_user(self,id:int):
        return self.db.query(UserModel).filter(UserModel.id == id).first()
    
    def get_user_by_email(self,email:str):
        return self.db.query(UserModel).filter(UserModel.email == email).first()
    
    def create_user(self,user:UserCreate):
        user.password = Auth().get_password(user.password)
        new_user = UserModel(**user.dict())
        self.db.add(new_user)
        self.db.commit()
        return
        