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
from relationship_state import State
from relationship_city import City, Base

if __name__ == '__main__':
    conn_str = f'mysql+mysqldb://{det[1]}:{det[2]}@localhost/{det[3]}'
    engine = create_engine(conn_str)
    Base.metadata.create_all(engine)
    session = Session(engine)
    new = State(name="California")
    new_city = City(name='San Francisco')
    new.cities.cities.append(new_city)
    session.add(new)
    session.commit()
    session.close()
