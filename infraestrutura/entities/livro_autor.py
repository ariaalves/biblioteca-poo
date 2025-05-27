from infraestrutura.configs.base import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

class LivroAutor(Base):

    __tablename__ = "livro_autor"
    id_livro = Column(Integer, ForeignKey("livro.id"), primary_key= True)
    id_autor = Column(Integer, ForeignKey("autor.id"), primary_key= True)
    
    livro = relationship("Livro", back_populates="livro_autores")
    autor = relationship("Autor", back_populates="livro_autores")



