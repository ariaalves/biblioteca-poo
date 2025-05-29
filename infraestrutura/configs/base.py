from sqlalchemy.orm import declarative_base, DeclarativeMeta, sessionmaker
from sqlalchemy import create_engine
from abc import ABCMeta

class BaseMeta(DeclarativeMeta, ABCMeta):
    pass

Base = declarative_base(metaclass=BaseMeta)
