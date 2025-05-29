from infraestrutura.repository.livro_repository import LivroRepository
from infraestrutura.repository.usuario_repository import UsuarioRepository
from infraestrutura.repository.editora_repository import EditoraRepository
from infraestrutura.repository.categoria_repository import CategoriaRepository
from infraestrutura.repository.autor_repository import AutorRepository
from infraestrutura.repository.emprestimo_repository import EmprestimoRepository
from infraestrutura.entities.usuario import Usuario
from datetime import date


livro_repo = LivroRepository()
usuario_repo = UsuarioRepository()
editora_repo = EditoraRepository()
categoria_repo = CategoriaRepository()
autor_repo = AutorRepository()
emprestimo_repo = EmprestimoRepository()


def menu():
    print("Bem-vindo ao SISTEMA DE BIBLIOTECA!")
    print("Ordem recomendada de cadastro:")
    print("1️ Usuário")
    print("2️ Editora")
    print("3️ Categoria")
    print("4️ Autor")
    print("5️ Livro")
    print("6️ Registrar Empréstimo\n")

    while True:
        print("\n=== SISTEMA DE BIBLIOTECA ===")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Registrar Empréstimo")
        print("4 - Listar Empréstimos")
        print("5 - Atualizar")
        print("6 - Deletar")
        print("7 - Consultar Tipo de Usuário")
        print("8 - Registrar Devolução")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case '1':
                menu_cadastrar()
            case '2':
                menu_listar()
            case '3':
                registrar_emprestimo()
            case '4':
                listar_emprestimos()
            case '5':
                menu_atualizar()
            case '6':
                menu_deletar()
            case '7':
                consultar_usuarios_por_tipo()
            case '8':
                registrar_devolucao()
            case '0':
                print("Encerrando o sistema.")
                break
            case _:
                print("Opção inválida!")


def input_id():
    try:
        return int(input("Informe o ID: "))
    except ValueError:
        print("ID inválido.")
        return None


def menu_cadastrar():
    tipo = input("Cadastrar (livro, usuario, editora, categoria, autor): ").strip().lower()
    match tipo:
        case "livro":
            if not (editora_repo.select() and categoria_repo.select() and autor_repo.select()):
                print("ALERTA! Antes de cadastrar um livro, cadastre pelo menos uma Editora, Categoria e Autor.")
                return
            titulo = input("Título: ")
            isbn = input("ISBN: ")
            ano = input("Ano: ")
            qtd = int(input("Quantidade: "))
            editora_id = int(input("ID da Editora: "))
            categoria_id = int(input("ID da Categoria: "))
            autor_id = int(input("ID do Autor: "))
            livro_repo.insert(titulo, isbn, ano, qtd, editora_id, categoria_id, autor_id)
            print("Livro cadastrado com sucesso.")
        case "usuario":
            nome = input("Nome: ")
            email = input("Email: ")
            tipo_usuario = input("Tipo (aluno/professor): ")
            usuario_repo.insert(nome, email, tipo_usuario)
            print("Usuário cadastrado com sucesso.")
            print(f"Total de usuários: {Usuario.contador}")
        case "editora":
            nome = input("Nome da Editora: ")
            editora_repo.insert(nome)
            print("Editora cadastrada com sucesso.")
        case "categoria":
            nome = input("Nome da Categoria: ")
            categoria_repo.insert(nome)
            print("Categoria cadastrada com sucesso.")
        case "autor":
            nome = input("Nome do Autor: ")
            nacionalidade = input("Nacionalidade: ")
            autor_repo.insert(nome, nacionalidade)
            print("Autor cadastrado com sucesso.")
        case _:
            print("Tipo inválido.")


def menu_listar():
    tipo = input("Listar (livro, usuario, editora, categoria, autor): ").strip().lower()
    match tipo:
        case "livro":
            listar_e_printar(livro_repo.select(), "LIVROS")
        case "usuario":
            listar_e_printar(usuario_repo.select(), "USUÁRIOS")
        case "editora":
            listar_e_printar(editora_repo.select(), "EDITORAS")
        case "categoria":
            listar_e_printar(categoria_repo.select(), "CATEGORIAS")
        case "autor":
            listar_e_printar(autor_repo.select(), "AUTORES")
        case _:
            print("Tipo inválido.")


def listar_e_printar(lista, titulo):
    print(f"\n--- {titulo} ---")
    for item in lista:
        print(item)


def registrar_emprestimo():
    if not (usuario_repo.select() and livro_repo.select()):
        print("ALERTA! Antes de registrar um empréstimo, cadastre pelo menos um Usuário e um Livro.")
        return

    data_str = input("Data do empréstimo (YYYY-MM-DD): ")
    usuario_id = int(input("ID do Usuário: "))
    livro_id = int(input("ID do Livro: "))
    try:
        ano, mes, dia = map(int, data_str.split("-"))
        data_obj = date(ano, mes, dia)
        emprestimo_repo.insert(data_obj, usuario_id, livro_id)
        print("Empréstimo registrado com sucesso.")
    except Exception as e:
        print(f"Data inválida ou erro no registro: {e}")


def listar_emprestimos():
    emprestimos = emprestimo_repo.select()
    print("\n--- EMPRÉSTIMOS ---")
    for emp in emprestimos:
        print(f"ID: {emp['id']} | Data: {emp['data']} | Usuário: {emp['usuario']} | Livro: {emp['livro']} | Devolução: {emp['data_devolucao'] or 'Pendente'}")


def registrar_devolucao():
    listar_emprestimos()
    id_ = input_id()
    if id_ is None:
        return
    data_str = input("Data da devolução (YYYY-MM-DD): ")
    try:
        ano, mes, dia = map(int, data_str.split("-"))
        data_devolucao = date(ano, mes, dia)
        emprestimo_repo.update(id_, data_devolucao)
        print("Devolução registrada com sucesso.")
    except Exception as e:
        print(f"Erro ao registrar devolução: {e}")


def menu_atualizar():
    tipo = input("Atualizar (livro, usuario, editora, categoria, autor): ").strip().lower()
    id_ = input_id()
    if id_ is None:
        return

    match tipo:
        case "livro":
            titulo = input("Novo Título: ")
            isbn = input("Novo ISBN: ")
            ano = input("Novo Ano: ")
            qtd = int(input("Nova Quantidade: "))
            editora_id = int(input("Novo ID da Editora: "))
            categoria_id = int(input("Novo ID da Categoria: "))
            autor_id = int(input("Novo ID do Autor: "))
            livro_repo.update(id_, titulo, isbn, ano, qtd, editora_id, categoria_id, autor_id)
            print("Livro atualizado com sucesso.")
        case "usuario":
            nome = input("Novo Nome: ")
            email = input("Novo Email: ")
            tipo_usuario = input("Novo Tipo (aluno/professor): ")
            usuario_repo.update(id_, nome, email, tipo_usuario)
            print("Usuário atualizado com sucesso.")
        case "editora":
            nome = input("Novo Nome: ")
            editora_repo.update(id_, nome)
            print("Editora atualizada com sucesso.")
        case "categoria":
            nome = input("Novo Nome: ")
            categoria_repo.update(id_, nome)
            print("Categoria atualizada com sucesso.")
        case "autor":
            nome = input("Novo Nome: ")
            nacionalidade = input("Nova Nacionalidade: ")
            autor_repo.update(id_, nome, nacionalidade)
            print("Autor atualizado com sucesso.")
        case _:
            print("Tipo inválido.")


def menu_deletar():
    tipo = input("Deletar (livro, usuario, editora, categoria, autor): ").strip().lower()
    id_ = input_id()
    if id_ is None:
        return

    match tipo:
        case "livro":
            livro_repo.delete(id_)
            print("Livro deletado.")
        case "usuario":
            usuario_repo.delete(id_)
            print("Usuário deletado.")
        case "editora":
            editora_repo.delete(id_)
            print("Editora deletada.")
        case "categoria":
            categoria_repo.delete(id_)
            print("Categoria deletada.")
        case "autor":
            autor_repo.delete(id_)
            print("Autor deletado.")
        case _:
            print("Tipo inválido.")


def consultar_usuarios_por_tipo():
    tipo = input("Tipo de usuário (ex: aluno, professor): ").strip().lower()
    usuarios = usuario_repo.select_by_tipo(tipo)
    if usuarios:
        print(f"\nUsuários do tipo '{tipo}':")
        for u in usuarios:
            print(f"ID: {u.id} | Nome: {u.nome} | Email: {u.email}")
    else:
        print("Nenhum usuário encontrado.")


if __name__ == "__main__":
    menu()
