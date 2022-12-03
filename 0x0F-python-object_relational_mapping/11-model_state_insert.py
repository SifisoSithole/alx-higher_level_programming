#!/usr/bin/python3

"""This script adds the State object “Louisiana” to the
database hbtn_0e_6_usa
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
    conn_string = f'mysql+mysqldb://{det[1]}:{det[2]}@localhost/{det[3]}'
    engine = create_engine(conn_string)
    Base.metadata.create_all(engine)
    session = Session(engine)
    new_user = State(name='Louisiana')
    session.add(new_user)
    session.commit()
    print(new_user.id)
    session.close()
