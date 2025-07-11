
from fastapi import FastAPI
from api import (
    clinica_router,
    veterinario_router,
    tutor_router,
    pet_router,
    atendimento_router
)

app = FastAPI()
app.include_router(clinica_router)
app.include_router(veterinario_router)
app.include_router(tutor_router)
app.include_router(pet_router)
app.include_router(atendimento_router)