from infraestrutura.configs.connection import DBConnetcion
from infraestrutura.entities.editora import Editora
from sqlalchemy.exc import IntegrityError

class EditoraRepository:
    def select(self):
        with DBConnetcion() as db:
            data = db.session.query(Editora).all()
            return data
        
    def insert (self, nome):
        with DBConnetcion() as db:
            try:
                data_insert = Editora(nome = nome)
                db.session.add(data_insert)
                db.session.commit()
            except IntegrityError as e:
                db.session.rollback()
                print(f"Erro de intregridade ao inserir editora: {e.orig}")
            except Exception as e:
                db.session.rollback()
                print(f"Erro ao inserir editora: {e}")
        
            
    def delete (self, id):
        with DBConnetcion() as db:
            db.session.query(Editora).filter(Editora.id == id).delete() 

    def update (self, id, novo_nome):
        with DBConnetcion() as db:
            db.session.query(Editora).filter(Editora.id == id).update({"nome" : novo_nome}) 
            db.session.commit()