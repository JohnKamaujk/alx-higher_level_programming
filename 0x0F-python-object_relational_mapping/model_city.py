#!/usr/bin/python3
"""
Contains City class definition
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    Class representing the cities table
    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False,
                primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
