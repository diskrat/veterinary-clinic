from fastapi import APIRouter

router = APIRouter()

@router.get("/clinicas")
async def list_clinicas():
    
    return [{"id": 1, "nome": "Clínica Exemplo"}]