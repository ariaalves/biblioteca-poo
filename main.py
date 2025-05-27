from infraestrutura.repository.livro_repository import LivroRepository
from infraestrutura.repository.usuario_repository import UsuarioRepository
from infraestrutura.repository.editora_repository import EditoraRepository
from infraestrutura.repository.categoria_repository import CategoriaRepository
from infraestrutura.repository.autor_repository import AutorRepository
from infraestrutura.repository.emprestimo_repository import EmprestimoRepository
from infraestrutura.repository.livro_autor import LivroAutor
from datetime import date

def main():
    # Criando instâncias dos repositórios
    livro_repo = LivroRepository()
    usuario_repo = UsuarioRepository()
    editora_repo = EditoraRepository()
    categoria_repo = CategoriaRepository()
    autor_repo = AutorRepository()
    emprestimo_repo = EmprestimoRepository()

    # Inserindo uma Editora
    editora_repo.insert("Companhia das Letras")

    # Inserindo uma Categoria
    categoria_repo.insert("Romance")

    # Inserindo um Autor
    autor_repo.insert("Isaac Asimov","Russo-americano")

    # Inserindo um Livro
    livro_repo.insert("Fundação", "123456789", date(1951, 1, 1), 6)

    # Inserindo um Usuário
    usuario_repo.insert("Ariany", "ari@email.com", "Leitor")

    # Realizando um Empréstimo
    emprestimo_repo.insert(date.today(), date(2025, 6, 1))

    # Consultas básicas
    print("Livros:")
    for livro in livro_repo.select():
        print(livro)

    print("\nUsuários:")
    for usuario in usuario_repo.select():
        print(usuario)

    print("\nEmpréstimos:")
    for emprestimo in emprestimo_repo.select():
        print(emprestimo)

if __name__ == "__main__":
    main()
