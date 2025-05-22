# 📚 Tema do Projeto: Biblioteca

## 🧱 Classes

- **Biblioteca** (Classe Abstrata)  
  Define a estrutura básica para uma biblioteca, exigindo a implementação do método `emprestar()`.

- **Livro** (herda de Biblioteca)  
  Representa um livro. Permite o registro de novos livros, o empréstimo e a devolução.

- **Pessoa** (Classe Abstrata)  
  Define os atributos básicos de uma pessoa (identificador e nome), exigindo a implementação do método `cadastrar()`.

- **Usuario** (herda de Pessoa)  
  Representa um usuário da biblioteca. Pode ser cadastrado e listado.

- **Fornecedor** (herda de Pessoa)  
  Representa fornecedores cadastrados, com métodos semelhantes aos do usuário.

## 🛠️ Como Executar

1. Certifique-se de que o Python 3 está instalado no seu sistema.
2. Salve o código como `classes.py`.
3. Execute no terminal com o comando:

```bash
python classes.py
```

O sistema criará um usuário de exemplo e imprimirá a lista de registros no console.

## ⚙️ Funcionalidades Principais

- Cadastro e listagem de **usuários** e **fornecedores**.
- Registro de **livros** com atributos como ISBN, título, gênero, autor e ano.
- **Empréstimo** e **devolução** de livros com controle de disponibilidade.

## 👨‍💻 Integrantes do Grupo

- Ariany Alves Silva  
- Erik Paulino Tertuliano  
- Heitor dos Santos Oliveira  
- Theofilo Fernandes de Mesquita

