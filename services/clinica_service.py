from repositories import ClinicaRepository
from models import Clinica

class ClinicaService:
    def __init__(self,clinica_repository:ClinicaRepository) -> None:
        self.clinica_repository = clinica_repository
    
    def create_clinica(self,id:int,nome:str,cidade:str):
        
        if self.clinica_repository.get_by_id(id):
            raise ValueError(f"Clínica com id '${id}' já existe.")
        
        new_clinica = Clinica(id,nome,cidade)
        return self.clinica_repository.create(new_clinica)    
        
    def get_clinica(self,id:int):
        clinica = self.clinica_repository.get_by_id(id)
        if not clinica:
            raise ValueError(f"Clínica com id '${id}' não existe.")
        return clinica

        
    def get_all(self):
        clinicas = self.clinica_repository.list_all()
        if not clinicas:
            raise ValueError(f"Não há clínicas cadastradas.")
        return clinicas
    
    def delete_clinica(self,id:int):
        clinica = self.clinica_repository.get_by_id(id)
        if not clinica:
            raise ValueError(f"Clínica com id '${id}' não existe.")
        self.clinica_repository.delete(clinica)
    
    def update_clinica(self,id:int,nome:str,cidade:str):
        old_clinica = self.clinica_repository.get_by_id(id)
        if not old_clinica:
            raise ValueError(f"Clínica com id '${id}' não existe.")

        edited_clinica = Clinica(id,nome,cidade)
        if old_clinica != edited_clinica:
           self.clinica_repository.update(edited_clinica)
        return edited_clinica