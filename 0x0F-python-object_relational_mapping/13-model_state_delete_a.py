#!/usr/bin/python3

"""This script deletes all State objects with a name
containing the letter a
Arguments:
    0: MySQL username
    1: MySQL password
    2: Database
"""

from sys import argv as det
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == '__main__':
    conn_str = f"mysql+mysqldb://{det[1]}:{det[2]}@localhost/{det[3]}"
    engine = create_engine(conn_str)
    Base.metadata.create_all(engine)
    session = Session(engine)
    session.query(State).filter(State.name.contains('a')).\
        delete(synchronize_session=False)
    session.commit()
    session.close()
