#tem que entender como vai ficar estruturado as operacoes nessa tb temp
from infraestrutura.configs.connection import DBConnetcion
from infraestrutura.entities.livro_autor import LivroAutor

class LivroAutorRepository:
    def select(self):
        with DBConnetcion() as db:
            data = db.session.query(LivroAutor).all()
            return data
        
    def insert (self, id_livro, id_autor):
        with DBConnetcion() as db:
            data_insert = LivroAutor(id_livro = id_livro, id_autor = id_autor)
            db.session.add(data_insert)
            db.session.commit()
            
    def delete (self, id_livro):
        with DBConnetcion() as db:
            db.session.query(LivroAutor).filter(LivroAutor.id_livro == id_livro).delete() #filtro para deletar pelo nome, verificar se a melhor opcao seria por id 
            db.session.commit()

    def update (self, id_livro, id_autor):
        with DBConnetcion() as db:
            db.session.query(LivroAutor).filter(LivroAutor.id_livro == id_livro).update(id_autor = id_autor) #cadastrado o emprestimo, para atualizar será necessário excluir, podendo alterar apenas a data de devolução
            db.session.commit()
    