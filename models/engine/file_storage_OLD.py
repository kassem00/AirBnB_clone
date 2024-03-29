#!/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
""" file storage class """

class FileStorage:
    """class storage"""
    __file_path = "file.json"
    __objects = dict
    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the __objects dictionary"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        o_to_dict = FileStorage.__objects
        objdict = dict

        for obj in o_to_dict.keys():
            objdict[obj] = o_to_dict[obj].to_dict()

        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)


    def reload(self):
        """
        Deserialize the JSON file specified by
        __file_path into __objects if it exists.
        """
        try:
            with open(FileStorage.__file_path) as file:
                serialized_objects = json.load(file)

                for serialized_obj in serialized_objects.values():
                    class_name = serialized_obj.pop("__class__", None)

                    if class_name:
                        obj_instance = eval(class_name)(**serialized_obj)
                        self.new(obj_instance)

        except FileNotFoundError:
            return
