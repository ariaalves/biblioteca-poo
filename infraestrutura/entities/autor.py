from infraestrutura.configs.base import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

class Autor(Base):

    __tablename__= "autor"
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable= False, unique = True)
    nacionalidade = Column(String, nullable= True)

    livros = relationship("Livro", back_populates="autor") 
    
    def __repr__(self):
        return f"<Autor(id={self.id}, nome='{self.nome}', nacionalidade='{self.nacionalidade}')>"