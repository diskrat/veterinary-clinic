from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from services.clinica import get_all_clinicas

router = APIRouter(prefix="/clinicas", tags=["Clinicas"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def listar_clinicas(db: Session = Depends(get_db)):
    return get_all_clinicas(db)
