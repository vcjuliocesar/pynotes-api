from models.note import Note as NoteModel
from schemas.note import Note

class NoteService():
    def __init__(self,db) -> None:
        self.db = db
        
    def get_notes(self):
        result = self.db.query(NoteModel).all()
        return result
    
    def get_note(self,id):
        result = self.db.query(NoteModel).filter(NoteModel.id == id).first()
        return result
    
    def create_note(self,data:Note):
        new_note = NoteModel(**data.dict())
        self.db.add(new_note)
        self.db.commit()
        return
    
    def update_note(self,id:int,data:Note):
        note = self.get_note(id)
        note.title = data.title
        note.content = data.content
        self.db.commit()
        return
    
    def delete_note(self,id:int):
        self.db.query(NoteModel).filter(NoteModel.id == id).delete()
        self.db.commit()
        return