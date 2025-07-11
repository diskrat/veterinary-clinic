from repositories import AtendimentoRepository
from models import Atendimento

class AtendimentoService:
    def __init__(self,atendimento_repository:AtendimentoRepository) -> None:
        self.atendimento_repository = atendimento_repository
    
    def get_by_pet(self,pet_id:int) -> list[Atendimento]:
        atendimentos = self.atendimento_repository.list_by_pet(pet_id)
        if not atendimentos:
            raise ValueError("Não há atendimentos cadastrados para este pet.")
        return atendimentos
    
    def create_atendimento(
        self,
        data,
        descricao:str,
        pet_id:int,
        veterinario_id:int
    )->Atendimento:
        new_atendimento = Atendimento(data,descricao,pet_id,veterinario_id)
        return self.atendimento_repository.create(new_atendimento)
    
    def get_all(self) -> list[Atendimento]:
        atendimentos = self.atendimento_repository.list_all()
        if not atendimentos:
            raise ValueError("Não há atendimentos cadastrados.")
        return atendimentos
    
    def get_by_veterinario(self,veterinario_id:int)-> list[Atendimento]:
        atendimentos = self.atendimento_repository.list_by_veterinario(veterinario_id)
        if not atendimentos:
            raise ValueError("Não há atendimentos para este veterinário.")
        return atendimentos