from sqlalchemy.orm import Session
from models import Atendimento

class AtendimentoRepository:
    def __init__(self, db:Session) -> None:
        self.db = db
        
    def list_by_pet(self,pet_id:int) -> list[Atendimento]:
        return self.db.query(
            Atendimento
        ).filter(
            Atendimento.pet_id==pet_id
        ).all()
    
    def create(self,atendimento:Atendimento)->Atendimento:
        self.db.add(atendimento)
        self.db.commit()
        self.db.refresh(atendimento)
        return atendimento

    def list_all(self) -> list[Atendimento]:
        return self.db.query(Atendimento).all()
    
    def list_by_veterinario(self,veterinario_id:int) -> list[Atendimento]:
        return self.db.query(
            Atendimento
        ).filter(
            Atendimento.veterinario_id == veterinario_id
        ).all()