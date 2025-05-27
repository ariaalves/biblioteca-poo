from infraestrutura.configs.connection import DBConnetcion
from infraestrutura.entities.livro import Livro
from sqlalchemy.exc import IntegrityError

class LivroRepository:
    def select(self):
        with DBConnetcion() as db:
            data = db.session.query(Livro).all()
            return data
        
    def insert (self, titulo, isbn, ano, qtd):
        with DBConnetcion() as db:
            try:
                data_insert = Livro(titulo = titulo, isbn = isbn, ano = ano, qtd = qtd)
                db.session.add(data_insert)
                db.session.commit()
            except IntegrityError as e:
                db.session.rollback()
                print(f"Erro de integridade ao inserir livro: {e.orig}")
            except Exception as e:
                db.session.rollback()
                print(f"Erro ao inserir livro: {e}")
            
    def delete (self, id):
        with DBConnetcion() as db:
            db.session.query(Livro).filter(Livro.id == id).delete()
            db.session.commit()

    def update (self, id, novo_titulo, novo_isbn, novo_ano):
        with DBConnetcion() as db:
            db.session.query(Livro).filter(Livro.id == id).update({"titulo": novo_titulo, "isbn": novo_isbn, "ano": novo_ano}) 
            db.session.commit()