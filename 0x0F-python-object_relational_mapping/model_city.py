#!/usr/bin/python3
"""Write a Python file that contains the class definition of a City.."""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


<<<<<<< HEAD
class City(Base):
=======
class State(Base):
>>>>>>> 6d048a36da541ad1e8740ae33b16a7809f0588ea
    """Inherits from Base links to the MySQL table cities."""

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
