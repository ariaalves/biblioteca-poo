from infraestrutura.repository.usuario_repository import UsuarioRepository


# repo.insert('Bianca', 'bianca@gmail.com', 'Aluno')

repo = UsuarioRepository()
response = repo.select_tipo()

print(response)
