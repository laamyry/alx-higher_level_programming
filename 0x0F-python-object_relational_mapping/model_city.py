#!/usr/bin/python3
"""contains the class definition of a State and an
instance Base = declarative_base()"""

from sys import argv
from sqlalchemy import create_engine as engine_c
from model_state import Base, State


if __name__ == "__main__":
    engine = engine_c('mysql+mysqldb://{}:{}@localhost/{}'
                      .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
