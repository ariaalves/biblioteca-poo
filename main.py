from infraestrutura.repository.livro_repository import LivroRepository
from infraestrutura.repository.usuario_repository import UsuarioRepository
from infraestrutura.repository.editora_repository import EditoraRepository
from infraestrutura.repository.categoria_repository import CategoriaRepository
from infraestrutura.repository.autor_repository import AutorRepository
from infraestrutura.repository.emprestimo_repository import EmprestimoRepository
from datetime import date

# repo = UsuarioRepository()
# repo.insert("Ariany", "ariariany093@gmail.com", "Aluno")
# response = repo.select()
# print(response)

# repo = EditoraRepository()
# repo.insert("Intrínseca")
# response = repo.select()
# print(response)

# repo = CategoriaRepository()
# repo.insert("Ficção")
# response = repo.select()
# print(response)

# repo = LivroRepository()
# repo.insert("Três Irmãs", "978-65-5560-664-5", "2024", 10, 1, 1, 1)
# response = repo.select()
# print(response)

repo = EmprestimoRepository()
repo.insert(date(2025, 5, 1), 1, 1)
response = repo.select()
print(response)

# repo = AutorRepository()
# repo.insert("Valérie Perrin", "Francesa")
# response = repo.select()
# print(response)

