from infraestrutura.configs.base import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

class Categoria(Base):

    __tablename__= "categoria"
    id = Column(Integer, primary_key=True)
    descricao = Column(String)
 