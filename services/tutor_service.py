
from repositories import TutorRepository
from models import Tutor

class TutorService:
    def __init__(self,tutor_repository: TutorRepository) -> None:
        self.tutor_repository = tutor_repository
    
    def create_tutor(self, nome: str, telefone: str):
        new_tutor = Tutor(nome,telefone)
        return self.tutor_repository.create(new_tutor)
    
