from models.note import Note as NoteModel
from schemas.note import Note,NoteBase,NoteCreate

class NoteService():
    
    def __init__(self,db) -> None:
    
        self.db = db
        
    def get_notes(self,owner_id:int):
    
        result = self.db.query(NoteModel).filter(NoteModel.owner_id == owner_id).all()
    
        return result
    
    def get_note(self,id:int,owner_id:int):
    
        result = self.db.query(NoteModel).filter((NoteModel.id == id) & (NoteModel.owner_id == owner_id)).first()
    
        return result
    
    def create_note(self,data:Note,owner_id:int):
    
        new_note = NoteModel(**data.dict(),owner_id = owner_id)
    
        self.db.add(new_note)
    
        self.db.commit()
    
        self.db.refresh(new_note)
    
        return
    
    def update_note(self,id:int,data:NoteBase,owner_id:int):
    
        note = self.get_note(id,owner_id)
    
        note.title = data.title
    
        note.content = data.content
    
        self.db.commit()
    
        return
    
    def delete_note(self,id:int,owner_id:int):
    
        self.db.query(NoteModel).filter((NoteModel.id == id) and (NoteModel.owner_id == owner_id)).delete()
    
        self.db.commit()
    
        return
    