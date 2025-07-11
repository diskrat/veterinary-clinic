from fastapi import APIRouter, Depends
from pydantic import BaseModel
from repositories import TutorRepository
from sqlalchemy.orm import Session
from api.dependencies import get_db
from services import TutorService

class TutorCreate(BaseModel):
    nome: str
    telefone: str

class TutorRead(BaseModel):
    id: int
    nome: str
    telefone: str
    
    model_config = {"from_attributes": True}
    
router = APIRouter()

@router.post("/tutores",response_model=TutorRead,status_code=201)
def create_tutor(tutor_in:TutorCreate,db:Session = Depends(get_db)):
    repo = TutorRepository(db)
    service = TutorService(repo)
    tutor = service.create_tutor(tutor_in.nome,tutor_in.telefone)
    return tutor