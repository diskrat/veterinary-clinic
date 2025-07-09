from sqlalchemy.orm import Session
from models.clinica import Clinica

class ClinicaRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, clinica: Clinica) -> Clinica:
        self.db.add(clinica)
        self.db.commit()
        self.db.refresh(clinica)
        return clinica

    def get_by_id(self, clinica_id: int) -> Clinica | None:
        return self.db.query(Clinica).filter(Clinica.id == clinica_id).first()

    
    def list_all(self) -> list[Clinica]:
        return self.db.query(Clinica).all()

    def delete(self, clinica: Clinica) -> None:
        self.db.delete(clinica)

    def update(self, clinica: Clinica) -> Clinica:
        self.db.merge(clinica)
        self.db.commit()
        self.db.refresh(clinica)
        return clinica
