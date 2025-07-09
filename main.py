from fastapi import FastAPI
from api.clinica_routes import router as clinica_router

app = FastAPI()
app.include_router(clinica_router)