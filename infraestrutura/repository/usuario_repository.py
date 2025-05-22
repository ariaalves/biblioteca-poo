from infraestrutura.configs.connection import DBConnetcion
from infraestrutura.entities.usuario import Usuario
from sqlalchemy.orm.exc import NoResultFound

class UsuarioRepository:

    def select(self):
        with DBConnetcion() as db:
            data = db.session.query(Usuario).all()
            return data
        
        #teste de excessao
    def select_tipo(self):
        with DBConnetcion() as db:
            try:
                data = db.session.query(Usuario).filter(Usuario.tipo == 'Fornecedor').one()
                return data
            except NoResultFound:
                return None
            except Exception as exception:
                db.session.rollback()
                raise exception
            
        
    def insert (self, nome, email, tipo):
        with DBConnetcion() as db:
            try:
                data_insert = Usuario(nome = nome, email = email, tipo = tipo)
                db.session.add(data_insert)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception
            
    def delete (self, nome):
        with DBConnetcion() as db:
            db.session.query(Usuario).filter(Usuario.nome == nome).delete() #filtro para deletar pelo nome, verificar se a melhor opcao seria por id 
            db.session.commit()

    def update (self, nome, email, tipo):
        with DBConnetcion() as db:
            db.session.query(Usuario).filter(Usuario.nome == nome).update(nome = nome, email = email, tipo = tipo) #filtro para deletar pelo nome, verificar se a melhor opcao seria por id e atualizando todos os dados do usuario 
            db.session.commit()



