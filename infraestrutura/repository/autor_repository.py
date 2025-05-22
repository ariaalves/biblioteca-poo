from infraestrutura.configs.connection import DBConnetcion
from infraestrutura.entities.autor import Autor

class AutorRepository:
    def select(self):
        with DBConnetcion() as db:
            data = db.session.query(Autor).all()
            return data
    
    def insert (self, nome, nacionalidade):
        with DBConnetcion() as db:
            data_insert = Autor(nome = nome, nacionalidade = nacionalidade)
            db.session.add(data_insert)
            db.session.commit()
            
    def delete (self, nome):
        with DBConnetcion() as db:
            db.session.query(Autor).filter(Autor.nome == nome).delete() #filtro para deletar pelo nome, verificar se a melhor opcao seria por id 
            db.session.commit()

    def update (self, nome, nacionalidade):
        with DBConnetcion() as db:
            db.session.query(Autor).filter(Autor.nome == nome).update(nome = nome, nacionalidade = nacionalidade) #filtro para deletar pelo nome, verificar se a melhor opcao seria por id e atualizando todos os dados do usuario 
            db.session.commit()



