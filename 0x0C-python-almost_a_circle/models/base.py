#!/usr/bin/python3
# base.py
"""Defines base model class."""
import json
import csv
import turtle


class Base:
    """Represent the base model.
    Represents the "base" for all other classes in the project.
    Attributes:
        __nb_objects (int): Keep track of id when object instantiated.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.
        Args:
            id (int): The identity of the new instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
