#!/usr/bin/python3

"""
Module: model_state
"""

import sys
from sqlalchemy import create_engine, Column, Integer, VARCHAR
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """Models a State in the USA. Tied to a database using sqlalchemy.
    Inherits from Base in declarative_base.
    """
    __tablename__ = "states"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", VARCHAR(128), nullable=False)


if __name__ == "__main__":
    db_type = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(
            db_type. format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True
            )
    Base.metadate.create_all(engine)
