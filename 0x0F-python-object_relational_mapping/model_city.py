#!/usr/bin/python3

"""
Module: model_city

Holds one class City()
"""

import sys
from sqlalchemy import create_engine, Column, Integer, ForeignKey, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from model_state import Base, State


class City(Base):
    """Models a city in the USA. Tied to a database using sqlalchemy.
    Inherits from Base in declarative_base.
    """
    __tablename__ = "cities"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", VARCHAR(128), nullable=False)
    state_id = Column(
            "state_id", Integer, ForeignKey("states.id"), nullable=False
            )

    state = relationship("State", back_populates="cities")


if __name__ == "__main__":
    db_type = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(
            db_type. format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True
            )
    Base.metadate.create_all(engine)
