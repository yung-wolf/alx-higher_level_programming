#!/usr/bin/python3

"""
Module: 14-model_city_fetch_by_state

Print all city objs from the database hbtn_0e_14_usa
"""

import sys
from sqlalchemy import create_engine, Column, Integer, ForeignKey, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    db_type = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(
            db_type. format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True
            )
    Base.metadata.bind = engine

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State, City).join(City).filter(
            State.id == City.state_id
            ).all()

    for state, city in result:
        print(f"{state.name}: ({city.id}) {city.name}")
