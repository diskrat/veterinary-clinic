from sqlalchemy.orm import Session
from repositories.clinica import get_all

def get_all_clinicas(db: Session):
    return get_all(db)
