from infraestrutura.configs.connection import DBConnetcion
from infraestrutura.entities.autor import Autor
from sqlalchemy.exc import IntegrityError

class AutorRepository:
    def select(self):
        with DBConnetcion() as db:
            data = db.session.query(Autor).all()
            return data
    
    def insert (self, nome, nacionalidade):
       with DBConnetcion() as db:
            try:
                data_insert = Autor(nome=nome, nacionalidade=nacionalidade)
                db.session.add(data_insert)
                db.session.commit()
            except IntegrityError as e:
                db.session.rollback()
                print(f"Erro de intregridade ao inserir autor: {e.orig}")
            except Exception as e:
                db.session.rollback()
                print(f"Erro ao inserir autor: {e}")
            
    def delete (self, id):
        with DBConnetcion() as db:
            db.session.query(Autor).filter(Autor.id == id).delete()  
            db.session.commit()

    def update (self, novo_nome, nova_nacionalidade):
        with DBConnetcion() as db:
            db.session.query(Autor).filter(Autor.id == id).update({"nome": novo_nome, "nacionalidade" : nova_nacionalidade}) 
            db.session.commit()



