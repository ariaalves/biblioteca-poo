from infraestrutura.configs.base import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship


class Editora(Base):

    __tablename__= "editora"
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    