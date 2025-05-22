from infraestrutura.configs.connection import DBConnetcion
from infraestrutura.entities.categoria import Categoria

class CategoriaRepository:
    def select(self):
        with DBConnetcion() as db:
            data = db.session.query(Categoria).all()
            return data
        
    def insert (self, nome):
        with DBConnetcion() as db:
            data_insert = Categoria(nome = nome)
            db.session.add(data_insert)
            db.session.commit()
            
    def delete (self, nome):
        with DBConnetcion() as db:
            db.session.query(Categoria).filter(Categoria.nome == nome).delete() #filtro para deletar pelo nome, verificar se a melhor opcao seria por id 
            db.session.commit()

    def update (self, nome):
        with DBConnetcion() as db:
            db.session.query(Categoria).filter(Categoria.nome == nome).update(nome = nome) #filtro para deletar pelo nome, verificar se a melhor opcao seria por id e atualizando todos os dados do usuario 
            db.session.commit()