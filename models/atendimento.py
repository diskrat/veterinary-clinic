from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Atendimento(Base):
    __tablename__ = 'atendimentos'

    id = Column(Integer, primary_key=True)
    data = Column(DateTime, nullable=False)
    descricao = Column(String, nullable=False)

    pet_id = Column(Integer, ForeignKey('pets.id'), nullable=False)
    pet = relationship('Pet', back_populates='atendimentos')

    veterinario_id = Column(Integer, ForeignKey('veterinarios.id'), nullable=False)
    veterinario = relationship('Veterinario', back_populates='atendimentos')
