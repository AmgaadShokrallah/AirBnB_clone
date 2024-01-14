#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represent an abstracted storage engine."""
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """
         Sets an object in the __objects dictionary with a key of
         <obj class name>.id.
        """
        obj_cls_name = obj.__class__.__name__

        key = "{}.{}".format(obj_cls_name, obj.id)

        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects as a JSON fiile """
        # print("saving into file.json")
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            my_dict = {}
            for key, obj in FileStorage.__objects.items():
                # object to dictionary
                my_dict[key] = obj.to_dict()
                # save myobj to a new dictionary, adding ascii
            json.dump(my_dict, f, ensure_ascii=False)

    def reload(self):
        """ deserializes JSON file to __objects dictionary  """
        # from models.base_model import BaseModel
        # from models import User, BaseModel
        diccionario = {"BaseModel": models.BaseModel, "User": models.User,
                       "State": models.State, "City": models.City,
                       "Amenity": models.Amenity, "Place": models.Place,
                       "Review": models.Review}
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                objs_dict = json.load(f)
            for key, objd in objs_dict.items():
                # print("objd ", objd)
                # FileStorage.__objects[key] = BaseModel(**objd)
                classname = objd["__class__"]
                FileStorage.__objects[key] = diccionario[classname](**objd)
