from sqlalchemy.orm import Session
from models import Pet

class PetRepository:
    def __init__(self,db:Session) -> None:
        self.db = db

    def list_by_tutor(self,tutor_id: int):
        return self.db.query(Pet).filter(Pet.tutor_id == tutor_id).all()
    
    def create(self,pet:Pet)->Pet:
        self.db.add(pet)
        self.db.commit()
        self.db.refresh(pet)
        return pet
    
    def list_all(self) -> list[Pet]:
        return self.db.query(Pet).all()
        