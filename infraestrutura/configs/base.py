from sqlalchemy.orm import declarative_base, DeclarativeMeta
from abc import ABCMeta

class BaseMeta(DeclarativeMeta, ABCMeta):
    pass

Base = declarative_base(metaclass=BaseMeta)