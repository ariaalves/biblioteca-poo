from infraestrutura.configs.connection import DBConnetcion
from infraestrutura.entities.emprestimo import Emprestimo
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload


class EmprestimoRepository:
    def select(self):
        with DBConnetcion() as db:
            emprestimos = db.session.query(Emprestimo)\
                .options(
                    joinedload(Emprestimo.usuario), 
                    joinedload(Emprestimo.livro)
                ).all()

            result = []
            for e in emprestimos:
                emprestimo_info = {
                    "id": e.id,
                    "data": e.data,
                    "data_devolucao": e.data_devolucao,
                    "usuario": e.usuario.nome if e.usuario else None,
                    "livro": e.livro.titulo if e.livro else None
                }
                result.append(emprestimo_info)
            return result
        
    def insert (self, data, id_usuario, id_livro, data_devolucao = None):
        with DBConnetcion() as db:
            try:            
                data_insert = Emprestimo(data = data, data_devolucao = data_devolucao, id_usuario = id_usuario, id_livro = id_livro)
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

    def update (self, id, data_devolucao):
        with DBConnetcion() as db:
            db.session.query(Emprestimo).filter(Emprestimo.id == id).update({"data_devolucao" : data_devolucao})
            db.session.commit()