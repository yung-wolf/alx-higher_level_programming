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
            with open(f"{cls.__name__}.json", "w") as file:
                json_str = cls.to_json_string([])
                file.write(json_str)
        else:
            with open(f"{cls.__name__}.json", "w") as file:
                for obj in list_objs:
                    json_list.append(obj.to_dictionary())  # adds obj json_list
                json_str = cls.to_json_string(json_list)
                file.write(json_str)

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
        from models.square import Square
        class_name = cls.__name__
        if class_name == 'Rectangle':
            dummy_rect = Rectangle(1, 1)
            dummy_rect.update(**dictionary)
            return dummy_rect
        elif class_name == 'Square':
            dummy_sq = Square(1)
            dummy_sq.update(**dictionary)
            return dummy_sq
        else:
            raise TypeError('Wrong class entered. Expected either '
                            'Rectangle or Square class')

    @classmethod
    def load_from_file(cls):
        """returns a list of instances from a json file"""
        class_name = cls.__name__
        if class_name == 'Rectangle':
            from models.rectangle import Rectangle
            list_rectangle = []
            with open(class_name + ".json", "r") as j_file:
                f_obj = json.load(j_file)  # change to file object
                for entry in f_obj:  # loop thru each entry in list(f_obj)
                    r1_json_str = Rectangle.to_json_string(entry)
                    r1_dic = Rectangle.from_json_string(r1_json_str)
                    r1 = Rectangle.create(**r1_dic)
                    list_rectangle.append(r1)  # add obj to list_rect... above
                return list_rectangle
        elif class_name == 'Square':
            from models.square import Square
            list_square = []
            with open(class_name + ".json", "r") as j_file:
                f_obj = json.load(j_file)
                for entry in f_obj:
                    sq1_json_str = Square.to_json_string(entry)
                    sq1_dic = Square.from_json_string(sq1_json_str)
                    sq1 = Square.create(**sq1_dic)
                    list_square.append(sq1)
                return list_square
        else:
            raise TypeError('Wrong class entered. Expected either '
                            'Rectangle or Square class')
