from sqlalchemy.orm import Session
from models import Tutor

class TutorRepository:
    def __init__(self,db:Session):
        self.db = db
    
    def create(self, tutor: Tutor) -> Tutor:
        self.db.add(tutor)
        self.db.commit()
        self.db.refresh(tutor)
        return tutor
    
    