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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts.
        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = str(cls.__name__) + ".json"

        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [obj.to_dictionary for obj in list_objs]
                list_json = Base.to_json_string(list_dicts)
                jsonfile.write(list_json)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation.
        Args:
            json_string (str): A JSON str representation of a list of dicts.
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a instance of cls from a dictionary of attributes.
        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_inst = cls(1, 1)
            else:
                new_inst = cls(1)
            new_inst.update(**dictionary)
            return new_inst

    @classmethod
    def load_from_file(cls):
        """Return a list of instances from a file of JSON strings.
        Reads from `<cls.__name__>.json`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"

        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**dict) for dict in list_dicts]
        except IOError:
            return []
