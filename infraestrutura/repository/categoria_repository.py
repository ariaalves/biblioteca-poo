from infraestrutura.configs.connection import DBConnetcion
from infraestrutura.entities.categoria import Categoria
from sqlalchemy.exc import IntegrityError

class CategoriaRepository:
    def select(self):
        with DBConnetcion() as db:
            data = db.session.query(Categoria).all()
            return data
        
    def insert (self, nome):
        with DBConnetcion() as db:
            try:
                data_insert = Categoria(nome = nome)
                db.session.add(data_insert)
                db.session.commit()
            except IntegrityError as e:
                db.session.rollback()
                print(f"Erro de intregridade ao inserir categoria: {e.orig}")
            except Exception as e:
                db.session.rollback()
                print(f"Erro ao inserir autor: {e}")
            
    def delete (self, id):
        with DBConnetcion() as db:
            db.session.query(Categoria).filter(Categoria.id == id).delete() 
            db.session.commit()

    def update (self, id, novo_nome):
        with DBConnetcion() as db:
            db.session.query(Categoria).filter(Categoria.id == id).update({"nome": novo_nome}) 
            db.session.commit()