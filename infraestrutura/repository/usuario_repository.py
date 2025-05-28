from infraestrutura.configs.connection import DBConnetcion
from infraestrutura.entities.usuario import Usuario
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import IntegrityError


class UsuarioRepository:

    def select(self):
        with DBConnetcion() as db:
            data = db.session.query(Usuario).all()
            return data
            
    def insert (self, nome, email, tipo):
        with DBConnetcion() as db:
            try:
                data_insert = Usuario(nome = nome, email = email, tipo = tipo)
                db.session.add(data_insert)
                db.session.commit()
            except IntegrityError as e:
                db.session.rollback()
                print(f"Erro de integridade ao inserir usuário: {e.orig}")
            except Exception as e:
                db.session.rollback()
                print(f"Erro ao inserir usuário: {e}")

    def delete (self, id):
        with DBConnetcion() as db:
            db.session.query(Usuario).filter(Usuario.id == id).delete()  
            db.session.commit()

    def update (self, id, novo_nome, novo_email, novo_tipo):
        with DBConnetcion() as db:
            db.session.query(Usuario).filter(Usuario.id == id).update({"nome": novo_nome, "email": novo_email, "tipo": novo_tipo}) 
            db.session.commit()



