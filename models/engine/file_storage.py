#!/usr/bin/python3
"""Module for class FileStorage"""

from models.user import User
from models.base_model import BaseModel
import json


class FileStorage:
    """
    A class that serializes instances to a JSON file and
    deserializes JSON file to instances.

    Attributes:
        __file_path (str): The path to the JSON file where objects are stored.
        __objects (dict): A dictionary of instantiated objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Gets all instantiated objects.

        Returns:
            dict: A dictionary of instantiated objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the storage dictionary.

        Args:
            obj (BaseModel): The object to be added to storage.
        """
        key = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(key, obj.id)] = obj

    def save(self):
        """
        Serializes the objects in the storage dictionary to a JSON file.
        """
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(objdict, f)

    def reload(self):
        """
        Deserializes the JSON file to objects if the JSON file
        (__file_path) exists.

        This method reads the JSON file, converts it back to
        a dictionary of objects,
        and restores them into the __objects dictionary,
        effectively reloading the
        stored objects into the application.
        """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                objdict = json.load(f)
                for obj_data in objdict.values():
                    cls_nam = obj_data['__class__']
                    del obj_data['__class__']
                    cls = globals()[cls_nam] if cls_nam in globals() else None
                    if cls:
                        self.new(cls(**obj_data))
        except FileNotFoundError:
            pass
