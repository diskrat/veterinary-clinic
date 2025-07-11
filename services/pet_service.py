from repositories import PetRepository
from models import Pet

class PetService:
    def __init__(self,pet_repository:PetRepository) -> None:
        self.pet_repository = pet_repository
    
    def create_pet(self,nome:str,especie:str,idade:int,tutor_id:int)->Pet:
        new_pet = Pet(nome,especie,idade,tutor_id)
        return self.pet_repository.create(new_pet)
    
    def get_all(self) -> list[Pet]:
        pets =self.pet_repository.list_all()
        if not pets:
            raise ValueError("Não há pets cadastrados.")
        return pets
    
    def get_by_tutor(self,tutor_id: int) -> list[Pet]:
        pets = self.pet_repository.list_by_tutor(tutor_id)
        if not pets:
            raise ValueError("Não há pets cadastrados para este tutor.")
        return pets