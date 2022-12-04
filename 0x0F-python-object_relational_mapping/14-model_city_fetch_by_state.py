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
from model_city import City

if __name__ == '__main__':
    conn_str = f'mysql+mysqldb://{det[1]}:{det[2]}@localhost/{det[3]}'
    engine = create_engine(conn_str)
    Base.metadata.create_all(engine)
    session = Session(engine)
    result = session.query(State, City).join(City).order_by(City.id).all()
    for stte, city in result:
        print(f'{stte.name}: ({city.id}) {city.name}')
    session.close()
