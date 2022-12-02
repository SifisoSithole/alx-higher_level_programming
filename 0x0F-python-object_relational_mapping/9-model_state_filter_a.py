#!/usr/bin/python3
"""This script lists all State objects that contain the letter a from
the database hbtn_0e_6_usa"""

from sys import argv as det
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import State, Base

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(det[1],
                           det[2], det[3]))
    Base.metadata.create_all(engine)
    session = Session(engine)
    for res in session.query(State).filter(State.name.contains('a')):
        print(f"{res.id}: {res.name}")

    session.close()
