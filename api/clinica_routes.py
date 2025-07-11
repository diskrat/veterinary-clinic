from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from repositories.clinica_repository import ClinicaRepository
from sqlalchemy.orm import Session
from api.dependencies import get_db
from services.clinica_service import ClinicaService

class ClinicaCreate(BaseModel):
    nome: str
    cidade: str

class ClinicaRead(BaseModel):
    id: int
    nome: str
    cidade: str

    model_config = {"from_attributes": True}

router = APIRouter()



@router.post("/clinicas", response_model=ClinicaRead, status_code=201)
def create_clinica(clinica_in: ClinicaCreate, db: Session = Depends(get_db)):
    repo = ClinicaRepository(db)
    service = ClinicaService(repo)
    clinica = service.create_clinica(clinica_in.nome, clinica_in.cidade)
    return clinica


@router.get("/clinicas", response_model=list[ClinicaRead])
def list_clinicas(db: Session = Depends(get_db)):
    repo = ClinicaRepository(db)
    service = ClinicaService(repo)
    try:
        return service.get_all()
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))



@router.get("/clinicas/{clinica_id}", response_model=ClinicaRead)
def get_clinica(clinica_id: int, db: Session = Depends(get_db)):
    repo = ClinicaRepository(db)
    service = ClinicaService(repo)
    try:
        clinica = service.get_clinica(clinica_id)
        return clinica
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))