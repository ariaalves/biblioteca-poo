from infraestrutura.configs.base import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from abc import ABC,  abstractmethod

class Pessoa(ABC):

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    @abstractmethod
    def exibir(self):
        pass

class Usuario(Base, Pessoa):

    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    email = Column(String)
    tipo = Column(String)

    contador = 0
    
    def __init__(self, nome, email, tipo):
        Pessoa.__init__(self, nome, email)
        self.tipo = tipo
        Usuario.contador_instancias()

    @classmethod
    def contador_instancias(cls):
        cls.contador += 1
    
    def exibir(self):
        print(f"Usuário: {self.nome}, Email: {self.email}")

    def __repr__(self):
        return f"<Usuario(id={self.id}, nome='{self.nome}', email='{self.email}', tipo='{self.tipo}')>"