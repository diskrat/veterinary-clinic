from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Tutor(Base):
    __tablename__ = 'tutores'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    telefone = Column(String, nullable=False)

    pets = relationship('Pet', back_populates='tutor')
