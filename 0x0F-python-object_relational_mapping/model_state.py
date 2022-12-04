#!/usr/bin/python3

"""
Creates a State model

Linked to a database
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class State(Base):
    """Represents a state in thye mysql database
    Parameters:
        __tablename__ (str): Name of the MySQL table
        id (int): The state's id
        name (str): The state's name
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='author')
