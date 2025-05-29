from infraestrutura.configs.base import Base
from sqlalchemy import Column, Integer, String
from abc import ABC, abstractmethod
from sqlalchemy.orm import relationship

class Pessoa(ABC):

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    @abstractmethod
    def realizar_acao_padrao(self):
        pass

class Usuario(Base, Pessoa):

    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    tipo = Column(String, nullable=False)

    contador = 0

    emprestimos = relationship("Emprestimo", back_populates="usuario")
    
    def __init__(self, nome, email, tipo):
        Pessoa.__init__(self, nome, email)
        self.tipo = tipo
        Usuario.contador_instancias()

    @classmethod
    def contador_instancias(cls):
        cls.contador += 1

    def realizar_acao_padrao(self):
        print(f"Ação padrão: registrando login do usuário '{self.nome}' ({self.email})")

    def __repr__(self):
        return f"<Usuario(id={self.id}, nome='{self.nome}', email='{self.email}', tipo='{self.tipo}')>"
