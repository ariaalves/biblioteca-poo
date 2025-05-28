from infraestrutura.configs.base import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship


class Emprestimo(Base):

    __tablename__= "emprestimo"
    id = Column(Integer, primary_key=True)
    data = Column(Date, nullable= False)
    data_devolucao = Column(Date, nullable= True)
    id_usuario = Column(Integer, ForeignKey("usuario.id"))
    id_livro = Column(Integer, ForeignKey("livro.id"))

    usuario = relationship("Usuario", back_populates="emprestimos")
    livro = relationship("Livro", back_populates="emprestimos")

    def __repr__(self):
        return f"<Emprestimo(id={self.id}, data_emprestimo='{self.data}', data_devolucao='{self.data_devolucao}')>"