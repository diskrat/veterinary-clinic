from sqlalchemy.orm import Session
from models import Veterinario

class VeterinarioRepository:
    def __init__(self, db: Session):
        self.db = db

    def list_by_clinica(self, clinica_id: int) -> list[Veterinario]:
        return self.db.query(Veterinario).filter(Veterinario.clinica_id == clinica_id).all()

    def create(self, veterinario: Veterinario) -> Veterinario:
        self.db.add(veterinario)
        self.db.commit()
        self.db.refresh(veterinario)
        return veterinario

    def list_all(self) -> list[Veterinario]:
        return self.db.query(Veterinario).all()

