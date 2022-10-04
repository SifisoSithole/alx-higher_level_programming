#!/usr/bin/python3
import json
import csv

"""
Define the ``Base`` class

The ``Base`` class is the base class of all the classes

it will be the super class for the Rectangle and Square class
"""


class Base:
    """
    Define a base class
    The ``Base`` class is the base class of all the classes
    it will be the super class for the Rectangle and Square class
    attributes:
        __nb_objects (int): handles automatic id assignment

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a ``Base`` instance
        Parameters:
            self (object): Object
            id (int): ID of the classes
        """

        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        """Returns JSON string represantation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the json string represantation of list_objs to a file"""
        if list_objs is None:
            list_dict = None
        else:
            list_dict = []
            for objs in list_objs:
                list_dict.append(objs.to_dictionary())

        filename = f"{cls.__name__}.json"
        with open(filename, 'w') as f:
            json.dump(list_dict, f)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation"""
        if json_string is None:
            return '[]'
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes"""
        s1 = object.__new__(cls)
        s1.__init__(10, 10)
        s1.update(**dictionary)
        return s1

    @classmethod
    def load_from_file(cls):
        """Retuns a list of instances"""
        filename = f"{cls.__name__}.json"
        with open(filename, "r") as f:
            if f is None:
                return []

            list_dict = json.load(f)

        inst_list = []
        for dictionary in list_dict:
            inst_list.append(cls.create(**dictionary))
        return inst_list
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves to csv file"""
        res = [item.to_dictionary() for item in list_objs]
        with open(cls.__name__ + ".csv", mode="w") as save_file:
            write_to = csv.DictWriter(save_file, res[0].keys())
            write_to.writeheader()
            write_to.writerows(res)

    @classmethod
    def load_from_file_csv(cls):
        """Loads from csv file"""
        res = []
        res_dict = {}
        with open(cls.__name__ + ".csv", mode="r") as read_file:
            read_from = csv.DictReader(read_file)
            for item in read_from:
                for k, v in dict(item).items():
                    res_dict[k] = int(v)
                # formatting with create()
                res.append(cls.create(**res_dict))
        return res
