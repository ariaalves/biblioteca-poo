from infraestrutura.configs.base import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship


class Emprestimo(Base):

    __tablename__= "emprestimo"
    id = Column(Integer, primary_key=True)
    data = Column(Date)
    data_devolucao = Column(Date)
    id_usuario = Column(Integer, ForeignKey("usuario.id"))
    id_livro = Column(Integer, ForeignKey("livro.id"))

    usuario = relationship("Usuario")
    livro = relationship("Livro")