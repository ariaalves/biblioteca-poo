from infraestrutura.configs.connection import DBConnetcion
from infraestrutura.entities.emprestimo import Emprestimo
from sqlalchemy.exc import IntegrityError

class EmprestimoRepository:
    def select(self):
        with DBConnetcion() as db:
            data = db.session.query(Emprestimo).all()
            return data
        
    def insert (self, data, data_devolucao):
        with DBConnetcion() as db:
            try:            
                data_insert = Emprestimo(data = data, data_devolucao = data_devolucao)
                db.session.add(data_insert)
                db.session.commit()
            except IntegrityError as e:
                db.session.rollback()
                print(f"Erro de integridade ao inserir empréstimo: {e.orig}")
            except Exception as e:
                db.session.rollback()
                print(f"Erro ao inserir empréstimo: {e}")

    def delete (self, id):
        with DBConnetcion() as db:
            db.session.query(Emprestimo).filter(Emprestimo.id == id).delete()
            db.session.commit()

    def update (self, id, nova_data, nova_data_devolucao):
        with DBConnetcion() as db:
            db.session.query(Emprestimo).filter(Emprestimo.id == id).update({"data" : nova_data, "data_devolucao" : nova_data_devolucao}) #cadastrado o emprestimo, para atualizar será necessário excluir, podendo alterar apenas a data de devolução
            db.session.commit()