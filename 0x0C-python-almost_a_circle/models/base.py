#!/usr/bin/python3

"""
Module: models/base
Holds one class, Base()
"""

import json


class Base:
    """Base class for all other classes in this project."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes object."""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            json_str = json.dumps(list_dictionaries)
            return json_str

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        from models.rectangle import Rectangle

        json_list = []  # empty list to hold dict of instances
        if list_objs is None:
            with open("class_name.json", "w") as j_file:
                json.dump('[]', j_file)
        else:
            if isinstance(list_objs[0], Rectangle):
                with open("Rectangle.json", "w") as j_file:
                    for obj in list_objs:
                        obj_dic = obj.to_dictionary()  # ch obj to dic
                        json_list.append(obj_dic)  # adds obj json_list
                    json.dump(cls.to_json_string(json_list), j_file)
            elif isinstance(list_objs[0], Square):
                with open("Square.json", "w") as j_file:
                    for obj in list_objs:
                        obj_dic = obj.to_dictionary()  # ch obj to dic
                        json_list.append(obj_dic)  # adds obj to list
                    json.dump(cls.to_json_string(json_list), j_file)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == "":
            return []
        else:
            obj = json.loads(json_string)
            return obj

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        from models.rectangle import Rectangle
        dummy_rect = Rectangle(1, 1)
        dummy_rect.update(**dictionary)
        return dummy_rect
