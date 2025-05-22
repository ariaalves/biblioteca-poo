from infraestrutura.configs.connection import DBConnetcion
from infraestrutura.entities.emprestimo import Emprestimo

class EmprestimoRepository:
    def select(self):
        with DBConnetcion() as db:
            data = db.session.query(Emprestimo).all()
            return data
        
    def insert (self, data, data_devolucao):
        with DBConnetcion() as db:
            data_insert = Emprestimo(data = data, data_devolucao = data_devolucao)
            db.session.add(data_insert)
            db.session.commit()
            
    def delete (self, data):
        with DBConnetcion() as db:
            db.session.query(Emprestimo).filter(Emprestimo.data == data).delete() #filtro para deletar pelo nome, verificar se a melhor opcao seria por id 
            db.session.commit()

    def update (self, data, data_devolucao):
        with DBConnetcion() as db:
            db.session.query(Emprestimo).filter(Emprestimo.data == data).update(data_devolucao = data_devolucao) #cadastrado o emprestimo, para atualizar será necessário excluir, podendo alterar apenas a data de devolução
            db.session.commit()