#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

det = sys.argv[1:]
if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(det[0],
                           det[1], det[2]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    states = session.query(State).order_by(State.id).all()
    print(len(states))
    for state in states:
        print(f"{state.id}: {state.name}")
