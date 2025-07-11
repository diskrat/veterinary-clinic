from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from repositories.veterinario_repositories import VeterinarioRepository
from sqlalchemy.orm import Session
from api.dependencies import get_db
from services.veterinario_service import VeterinarioService

class VeterinarioCreate(BaseModel):
    nome: str
    especialidade: str
    clinica_id: int


class VeterinarioRead(BaseModel):
    id: int
    nome: str
    especialidade: str
    clinica_id: int

    model_config = {"from_attributes": True}

router = APIRouter()

# Get all veterinarios from a single clinic
@router.get("/clinicas/{clinica_id}/veterinarios", response_model=list[VeterinarioRead])
def get_veterinarios_by_clinica(clinica_id: int, db: Session = Depends(get_db)):
    repo = VeterinarioRepository(db)
    service = VeterinarioService(repo)
    try:
        veterinarios = service.get_by_clinica(clinica_id)
        return veterinarios
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/veterinarios", response_model=VeterinarioRead, status_code=201)
def create_veterinario(vet_in: VeterinarioCreate, db: Session = Depends(get_db)):
    repo = VeterinarioRepository(db)
    service = VeterinarioService(repo)
    veterinario = service.create_veterinario(vet_in.nome, vet_in.especialidade, vet_in.clinica_id)
    return veterinario


# Example: List all veterinarios
@router.get("/veterinarios", response_model=list[VeterinarioRead])
def list_veterinarios(db: Session = Depends(get_db)):
    repo = VeterinarioRepository(db)
    service = VeterinarioService(repo)
    try:
        return service.get_all()
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
