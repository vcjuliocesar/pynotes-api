from models.user import User as UserModel
from schemas.user import User

class UserService():
    def __init__(self,db) -> None:
        self.db = db
        
    def get_users(self):
        result = self.db.query(UserModel).all()
        return result
    
    def get_user(self,id):
        result = self.db.query(UserModel).filter(UserModel.id == id).first()
        return result
    
    def create_user(self,data:User):
        new_user = UserModel(**data.dict())
        self.db.add(new_user)
        self.db.commit()
        return
    
    def update_user(self,id:int,data:User):
        user = self.get_user(id)
        user.email = data.email
        user.password = data.password
        self.db.commit()
        return
    
    def delete_user(self,id:int):
        self.db.query(UserModel).filter(UserModel.id == id).delete()
        self.db.commit()
        return
    
    def find_user_by_email(self,email:str):
        return self.db.query(UserModel).filter(UserModel.email == email).first()