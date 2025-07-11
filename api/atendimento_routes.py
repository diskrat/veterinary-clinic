from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from repositories import AtendimentoRepository
from sqlalchemy.orm import Session
from api.dependencies import get_db
from services import AtendimentoService

class AtendimentoCreate(BaseModel):
    data: datetime
    descricao: str
    pet_id:int
    veterinario_id:int
    
class AtendimentoRead(BaseModel):
    id: int
    data: datetime
    descricao: str
    pet_id: int
    veterinario_id: int
    
    model_config = {"from_attributes": True}

router = APIRouter()

@router.get("/pets/{pet_id}/atendimentos", response_model=list[AtendimentoRead])
def get_atendimentos_by_pet(pet_id: int, db: Session = Depends(get_db)):
    repo = AtendimentoRepository(db)
    service = AtendimentoService(repo)
    try:
        atendimentos = service.get_by_pet(pet_id)
        return atendimentos
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/atendimentos", response_model=AtendimentoRead, status_code=201)
def create_atendimento(atendimento_in: AtendimentoCreate, db: Session = Depends(get_db)):
    repo = AtendimentoRepository(db)
    service = AtendimentoService(repo)
    atendimento = service.create_atendimento(
        atendimento_in.data,
        atendimento_in.descricao,
        atendimento_in.pet_id,
        atendimento_in.veterinario_id
    )
    return atendimento

@router.get("/atendimentos", response_model=list[AtendimentoRead])
def list_atendimentos(db: Session = Depends(get_db)):
    repo = AtendimentoRepository(db)
    service = AtendimentoService(repo)
    try:
        return service.get_all()
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/veterinarios/{veterinario_id}/atendimentos", response_model=list[AtendimentoRead])
def get_atendimentos_by_veterinario(veterinario_id: int, db: Session = Depends(get_db)):
    repo = AtendimentoRepository(db)
    service = AtendimentoService(repo)
    try:
        atendimentos = service.get_by_veterinario(veterinario_id)
        return atendimentos
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))