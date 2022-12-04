#!/usr/bin/python3
"""
Defines a City class

Represents a city in a state
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    Represention of a city in a state
    Attributes:
        __tablename__ (String): Table name
        id (Integer): a column of an auto-generated, unique integer,
                      can’t be null and is a primary key.
        name (String): represents a column of a string of
                       128 characters and can’t be null.
        state_id (Integer): represents a column of an integer, can’t
                            be null and is a foreign key to states.id
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"))
