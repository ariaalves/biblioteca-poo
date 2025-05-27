from infraestrutura.configs.base import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship


class Editora(Base):

    __tablename__= "editora"
    id = Column(Integer, primary_key=True)
    nome = Column(String)

    livros = relationship("Livro", back_populates="editora")    

    def __repr__(self):
        return f"<Editora(id={self.id}, nome='{self.nome}')>"
    