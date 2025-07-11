from repositories import VeterinarioRepository
from models import Veterinario

class VeterinarioService:
    def __init__(self,veterinario_repository:VeterinarioRepository) -> None:
        self.veterinario_repository = veterinario_repository
    
    def create_veterinario(self, nome: str, especialidade: str, clinica_id: int) -> Veterinario:
        new_veterinario = Veterinario(nome=nome, especialidade=especialidade, clinica_id=clinica_id)
        return self.veterinario_repository.create(new_veterinario)
        
    def get_all(self) -> list[Veterinario]:
        veterinarios = self.veterinario_repository.list_all()
        if not veterinarios:
            raise ValueError("Não há veterinários cadastrados.")
        return veterinarios

    def get_by_clinica(self, clinica_id: int) -> list[Veterinario]:
        veterinarios = self.veterinario_repository.list_by_clinica(clinica_id)
        if not veterinarios:
            raise ValueError("Não há clínicas cadastradas para este veterinário.")
        return veterinarios
