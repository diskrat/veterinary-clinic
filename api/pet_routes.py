from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from repositories import PetRepository
from sqlalchemy.orm import Session
from api.dependencies import get_db
from services import PetService

class PetCreate(BaseModel):
    nome: str
    especie: str
    idade: int
    tutor_id: int

class PetRead(BaseModel):
    id: int
    nome: str
    especie: str
    idade: int
    tutor_id: int
    
    model_config = {"from_attributes": True}
    
router = APIRouter()

@router.get("/tutores/{tutor_id}/pets",response_model=list[PetRead])
def get_pet_by_tutor(tutor_id:int,db:Session = Depends(get_db)):
    repo = PetRepository(db)
    service = PetService(repo)
    try:
        pets = service.get_by_tutor(tutor_id)
        return pets
    except ValueError as e:
        raise HTTPException(status_code=404,detail=str(e))
    
@router.post("/pets",response_model=PetRead,status_code=201)
def create_pet(pet_in:PetCreate,db:Session = Depends(get_db)):
    repo = PetRepository(db)
    service = PetService(repo)
    veterinario = service.create_pet(
        pet_in.nome,
        pet_in.especie,
        pet_in.idade,
        pet_in.tutor_id
    )
    return veterinario

@router.get("/pets",response_model=list[PetRead])
def list_pets(db:Session=Depends(get_db)):
    repo = PetRepository(db)
    service = PetService(repo)
    try:
        return service.get_all()
    except ValueError as e:
        raise HTTPException(status_code=404,detail=str(e))


        
    
    

