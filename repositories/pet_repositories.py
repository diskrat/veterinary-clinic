from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Pet(Base):
    __tablename__ = 'pets'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    especie = Column(String, nullable=False)
    idade = Column(Integer, nullable=False)

    tutor_id = Column(Integer, ForeignKey('tutores.id'), nullable=False)
    tutor = relationship('Tutor', back_populates='pets')

    atendimentos = relationship('Atendimento', back_populates='pet')
