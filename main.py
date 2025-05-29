from infraestrutura.repository.livro_repository import LivroRepository
from infraestrutura.repository.usuario_repository import UsuarioRepository
from infraestrutura.repository.editora_repository import EditoraRepository
from infraestrutura.repository.categoria_repository import CategoriaRepository
from infraestrutura.repository.autor_repository import AutorRepository
from infraestrutura.repository.emprestimo_repository import EmprestimoRepository
from infraestrutura.configs.connection import DBConnetcion
from infraestrutura.entities.usuario import Usuario
from sqlalchemy.exc import IntegrityError
from datetime import date

livro_repo = LivroRepository()
usuario_repo = UsuarioRepository()
editora_repo = EditoraRepository()
categoria_repo = CategoriaRepository()
autor_repo = AutorRepository()
emprestimo_repo = EmprestimoRepository()

def menu():
    while True:
        print("\n SISTEMA DE BIBLIOTECA")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Registrar Empréstimo")
        print("4 - Listar Empréstimos")
        print("5 - Atualizar")
        print("6 - Deletar")
        print("7 - Consultar Tipo de Usuário")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar()
        elif opcao == '2':
            listar()
        elif opcao == '3':
            registrar_emprestimo()
        elif opcao == '4':
            listar_emprestimos()
        elif opcao == '5':
            atualizar()
        elif opcao == '6':
            deletar()
        elif opcao == '7':
            consultar_usuarios_por_tipo()
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

def cadastrar():
    tipo = input("O que deseja cadastrar (livro, usuario, editora, categoria, autor)? ").strip().lower()

    if tipo == "livro":
        titulo = input("Título: ")
        isbn = input("ISBN: ")
        ano = input("Ano: ")
        qtd = int(input("Quantidade: "))
        editora_id = int(input("ID da Editora: "))
        categoria_id = int(input("ID da Categoria: "))
        autor_id = int(input("ID do Autor: "))
        livro_repo.insert(titulo, isbn, ano, qtd, editora_id, categoria_id, autor_id)
        print(" Livro cadastrado com sucesso.")
    
    elif tipo == "usuario":
        nome = input("Nome: ")
        email = input("Email: ")
        tipo_usuario = input("Tipo de usuário (ex: aluno, professor): ")
        usuario_repo.insert(nome, email, tipo_usuario)
        print("Usuário cadastrado com sucesso.")
        print(f"Total de usuários criados: {Usuario.contador}")
    
    elif tipo == "editora":
        nome = input("Nome da Editora: ")
        editora_repo.insert(nome)
        print("Editora cadastrada com sucesso.")
    
    elif tipo == "categoria":
        nome = input("Nome da Categoria: ")
        categoria_repo.insert(nome)
        print("Categoria cadastrada com sucesso.")
    
    elif tipo == "autor":
        nome = input("Nome do Autor: ")
        nacionalidade = input("Nacionalidade: ")
        autor_repo.insert(nome, nacionalidade)
        print("Autor cadastrado com sucesso.")
    
    else:
        print("Tipo inválido.")

def listar():
    tipo = input("O que deseja listar (livro, usuario, editora, categoria, autor)? ").strip().lower()

    if tipo == "livro":
        livros = livro_repo.select()
        print("\n--- LIVROS ---")
        for l in livros:
            print(l)
    
    elif tipo == "usuario":
        usuarios = usuario_repo.select()
        print("\n--- USUÁRIOS ---")
        for u in usuarios:
            print(u)
    
    elif tipo == "editora":
        editoras = editora_repo.select()
        print("\n--- EDITORAS ---")
        for e in editoras:
            print(e)
    
    elif tipo == "categoria":
        categorias = categoria_repo.select()
        print("\n--- CATEGORIAS ---")
        for c in categorias:
            print(c)
    
    elif tipo == "autor":
        autores = autor_repo.select()
        print("\n--- AUTORES ---")
        for a in autores:
            print(a)
    
    else:
        print("Tipo inválido.")

def registrar_emprestimo():
    data_str = input("Data do empréstimo (YYYY-MM-DD): ")
    usuario_id = int(input("ID do Usuário: "))
    livro_id = int(input("ID do Livro: "))
    ano, mes, dia = map(int, data_str.split("-"))
    data_obj = date(ano, mes, dia)
    emprestimo_repo.insert(data_obj, usuario_id, livro_id)
    print("Empréstimo registrado.")

def listar_emprestimos():
    emprestimos = emprestimo_repo.select()
    print("\n--- EMPRÉSTIMOS ---")
    for emp in emprestimos:
        print(f"ID: {emp['id']} | Data: {emp['data']} | Usuário: {emp['usuario']} | Livro: {emp['livro']} | Devolução: {emp['data_devolucao'] or 'Pendente'}")

def atualizar():
    tipo = input("O que deseja atualizar (livro, usuario, editora, categoria, autor)? ").strip().lower()
    id_ = int(input("Informe o ID: "))

    if tipo == "livro":
        titulo = input("Novo Título: ")
        isbn = input("Novo ISBN: ")
        ano = input("Novo Ano: ")
        qtd = int(input("Nova Quantidade: "))
        editora_id = int(input("Novo ID da Editora: "))
        categoria_id = int(input("Novo ID da Categoria: "))
        autor_id = int(input("Novo ID do Autor: "))
        livro_repo.update(id_, titulo, isbn, ano, qtd, editora_id, categoria_id, autor_id)
        print("Livro atualizado com sucesso.")
    
    elif tipo == "usuario":
        nome = input("Novo Nome: ")
        email = input("Novo Email: ")
        tipo_usuario = input("Novo Tipo de usuário: ")
        usuario_repo.update(id_, nome, email, tipo_usuario)
        print("Usuário atualizado com sucesso.")
    
    elif tipo == "editora":
        nome = input("Novo Nome da Editora: ")
        editora_repo.update(id_, nome)
        print("Editora atualizada com sucesso.")
    
    elif tipo == "categoria":
        nome = input("Novo Nome da Categoria: ")
        categoria_repo.update(id_, nome)
        print("Categoria atualizada com sucesso.")
    
    elif tipo == "autor":
        nome = input("Novo Nome do Autor: ")
        nacionalidade = input("Nova Nacionalidade: ")
        autor_repo.update(id_, nome, nacionalidade)
        print("Autor atualizado com sucesso.")
    
    else:
        print("Tipo inválido.")

def deletar():
    tipo = input("O que deseja deletar (livro, usuario, editora, categoria, autor)? ").strip().lower()
    id_ = int(input("Informe o ID para deletar: "))

    if tipo == "livro":
        livro_repo.delete(id_)
        print("Livro deletado com sucesso.")
    elif tipo == "usuario":
        usuario_repo.delete(id_)
        print("Usuário deletado com sucesso.")
    elif tipo == "editora":
        editora_repo.delete(id_)
        print("Editora deletada com sucesso.")
    elif tipo == "categoria":
        categoria_repo.delete(id_)
        print("Categoria deletada com sucesso.")
    elif tipo == "autor":
        autor_repo.delete(id_)
        print("Autor deletado com sucesso.")
    else:
        print("Tipo inválido.")

def consultar_usuarios_por_tipo():
    tipo = input("Informe o tipo de usuário (ex: aluno, professor): ").strip().lower()
    usuarios = usuario_repo.select_by_tipo(tipo)
    if usuarios:
        print(f"\nUsuários do tipo '{tipo}':")
        for u in usuarios:
            print(f"ID: {u.id} | Nome: {u.nome} | Email: {u.email}")
    else:
        print("Nenhum usuário encontrado para esse tipo.")

if __name__ == "__main__":
    menu()