from infraestrutura.configs.base import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

class Autor(Base):

    __tablename__= "autor"
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    nacionalidade = Column(String)