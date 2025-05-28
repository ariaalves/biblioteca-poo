from infraestrutura.configs.connection import DBConnetcion
from infraestrutura.entities.livro import Livro
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload

class LivroRepository:
    def select(self):
        with DBConnetcion() as db:
           livros = db.session.query(Livro)\
                .options(
                    joinedload(Livro.editora),
                    joinedload(Livro.categoria),
                    joinedload(Livro.autor)
            ).all()

        result = []
           
        for l in livros:
            livro_info = {
                "id": l.id,
                "titulo": l.titulo,
                "ano": l.ano,
                "isbn": l.isbn,
                "qtd": l.qtd,
                "editora": l.editora.nome if l.editora else None,
                "categoria": l.categoria.nome if l.categoria else None,
                "autor": l.autor.nome if l.autor else None
            }
            result.append(livro_info)
            return result
        
    
    def insert (self, titulo, isbn, ano, qtd, id_editora, id_categoria, id_autor):
        with DBConnetcion() as db:
            try:
                data_insert = Livro(titulo = titulo, isbn = isbn, ano = ano, qtd = qtd, id_editora = id_editora, id_categoria = id_categoria, id_autor = id_autor)
                db.session.add(data_insert)
                db.session.commit()
            except IntegrityError as e:
                db.session.rollback()
                print(f"Erro de integridade ao inserir livro: {e.orig}")
            except Exception as e:
                db.session.rollback()
                print(f"Erro ao inserir livro: {e}")
            
    def delete (self, id):
        with DBConnetcion() as db:
            db.session.query(Livro).filter(Livro.id == id).delete()
            db.session.commit()

    def update (self, id, novo_titulo, novo_isbn, novo_ano):
        with DBConnetcion() as db:
            db.session.query(Livro).filter(Livro.id == id).update({"titulo": novo_titulo, "isbn": novo_isbn, "ano": novo_ano}) 
            db.session.commit()