from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnetcion:
    def __init__(self):
        self.__connection_string = 'sqlite:///biblioteca.db' #conexao com o banco criado
        self.__engine = self.__create_database_engine() # criação do banco
        self.session = None #operacoes

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine
    
    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session_make = sessionmaker(bind= self.__engine)#pesquisar o uso do bind, abrir uma sessao
        self.session = session_make()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb): 
        self.session.close()#fechamento da sessao
