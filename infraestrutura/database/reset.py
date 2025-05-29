from infraestrutura.configs.connection import DBConnetcion
from infraestrutura.configs.base import Base
from infraestrutura.entities.autor import Autor
from infraestrutura.entities.livro import Livro
from infraestrutura.entities.usuario import Usuario
from infraestrutura.entities.editora import Editora
from infraestrutura.entities.categoria import Categoria
from infraestrutura.entities.emprestimo import Emprestimo

import os

def resetar_banco():
    if os.path.exists("biblioteca.db"):
        print("Removendo banco anterior...")
        os.remove("biblioteca.db")

    print("Criando novo banco de dados...")
    connection = DBConnetcion()
    engine = connection.get_engine()

    Base.metadata.create_all(bind=engine)
    print("Banco de dados recriado com sucesso.")

if __name__ == "__main__":
    resetar_banco()