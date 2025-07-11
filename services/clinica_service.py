from repositories import ClinicaRepository
from models import Clinica

class ClinicaService:
    def __init__(self,clinica_repository:ClinicaRepository) -> None:
        self.clinica_repository = clinica_repository
    
    def create_clinica(self, nome: str, cidade: str) -> Clinica:
        new_clinica = Clinica(nome=nome, cidade=cidade)
        return self.clinica_repository.create(new_clinica)
        
    def get_clinica(self,id:int) -> Clinica:
        clinica = self.clinica_repository.get_by_id(id)
        if not clinica:
            raise ValueError(f"Clínica com id '${id}' não existe.")
        return clinica

        
    def get_all(self) -> list[Clinica]:
        clinicas = self.clinica_repository.list_all()
        if not clinicas:
            raise ValueError(f"Não há clínicas cadastradas.")
        return clinicas