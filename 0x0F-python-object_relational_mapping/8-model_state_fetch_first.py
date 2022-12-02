#!/usr/bin/python3
"""This script prints the first State object from the database
hbtn_0e_6_usa"""

from sys import argv as det
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(det[1],
                           det[2], det[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    result = session.query(State).order_by(State.id).first()
    if result is None:
        print("Nothing")
    else:
        print(f"{result.id}: {result.name}")
