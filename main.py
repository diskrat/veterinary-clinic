from fastapi import FastAPI
from database import engine
from models import base
from api import clinica_routes

base.Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url="/docs", redoc_url="/redoc")

app.include_router(clinica_routes.router)
