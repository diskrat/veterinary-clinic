from sqlalchemy.orm import Session
from models.clinica import Clinica

def get_all(db: Session):
    return db.query(Clinica).all()
