#!/usr/bin/python3

"""This script lists all cities from the database hbtn_0e_4_usa
Arguments:
    0: MySQL username
    1: MySQL password
    2: Database
    3: State name to search
"""

from sys import argv as det
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == '__main__':
    string = f'mysql+mysqldb://{det[1]}:{det[2]}@localhost/{det[3]}'
    engine = create_engine(string)
    Base.metadata.create_all(engine)
    session = Session(engine)
    result = session.query(State).filter(State.name == det[4]).first()
    if result is None:
        print("Not found")
    else:
        print(result.id)
    session.close()
