from infraestrutura.configs.base import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

class Categoria(Base):

    __tablename__= "categoria"
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable= False, unique= True)

    livros = relationship("Livro", back_populates="categoria")

    def __repr__(self):
        return f"<Categoria(id={self.id}, nome='{self.nome}')>"
 