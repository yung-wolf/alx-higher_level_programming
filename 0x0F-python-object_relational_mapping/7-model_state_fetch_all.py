#!/usr/bin/python3

"""
Module: 7-model_state_fetchall

Fetch all state objs from db hbtn_0e_6_usa
"""

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine, Table, MetaData
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    Base = declarative_base()

    db_type = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(
            db_type.format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True
            )

    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in session.query(State).order_by(State.id):
        print(f"{instance.id}: {instance.name}")
