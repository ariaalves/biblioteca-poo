from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

class DBConnetcion:
    def __init__(self):
        self.__connection_string = 'sqlite:///biblioteca.db'
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(
            self.__connection_string,
            connect_args={"check_same_thread": False} 
        )
        # with engine.connect() as connection:
        #     connection.execute(text("PRAGMA journal_mode=WAL"))
        return engine
    
    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb): 
        self.session.close()
