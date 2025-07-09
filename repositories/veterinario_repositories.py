from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Veterinario(Base):
    __tablename__ = 'veterinarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    especialidade = Column(String, nullable=False)

    clinica_id = Column(Integer, ForeignKey('clinicas.id'), nullable=False)
    clinica = relationship('Clinica', back_populates='veterinarios')

    atendimentos = relationship('Atendimento', back_populates='veterinario')
