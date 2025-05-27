from infraestrutura.configs.base import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

class Livro(Base):

    __tablename__= "livro"
    id = Column(Integer, primary_key=True)
    ano = Column(Date)
    titulo = Column(String)
    isbn = Column(String)
    __qtd = Column("qtd",Integer)

    id_editora = Column(Integer, ForeignKey("editora.id"))
    id_categoria = Column(Integer, ForeignKey("categoria.id"))

    editora = relationship("Editora", back_populates="livros")
    categoria = relationship("Categoria", back_populates="livros")

    livro_autores = relationship("LivroAutor", back_populates="livro")

    emprestimos = relationship("Emprestimo", back_populates="livro")



    @property
    def qtd(self):
        return self.__qtd

    @qtd.setter
    def qtd(self, valor):
        if valor < 0:
            raise ValueError("Quantidade de livros não pode ser negativa.")
        self.__qtd = valor

    def qtd_livro(self):
        if self.qtd == 0:
            print("Livro indisponível no momento, necessário reposição")
        else:
            print("Livro disponível")

    def __repr__(self):
         return f"<Livro(id={self.id}, titulo='{self.titulo}', ano='{self.ano}', isbn='{self.isbn}'. quantidade='{self.qtd}')>"
