from infraestrutura.configs.connection import DBConnetcion
from infraestrutura.entities.livro import Livro

class LivroRepository:
    def select(self):
        with DBConnetcion() as db:
            data = db.session.query(Livro).all()
            return data
        
    def insert (self, titulo, isbn, ano):
        with DBConnetcion() as db:
            data_insert = Livro(titulo = titulo, isbn = isbn, ano = ano)
            db.session.add(data_insert)
            db.session.commit()
            
    def delete (self, titulo):
        with DBConnetcion() as db:
            db.session.query(Livro).filter(Livro.titulo == titulo).delete() #filtro para deletar pelo titulo, verificar se a melhor opcao seria por isbn
            db.session.commit()

    def update (self, titulo, isbn, ano):
        with DBConnetcion() as db:
            db.session.query(Livro).filter(Livro.titulo == titulo).update(titulo = titulo, isbn = isbn, ano = ano) #filtro para deletar pelo nome, verificar se a melhor opcao seria por isbn
            db.session.commit()