#!/usr/bin/python3
"""Module for BaseModel"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    def __init__(self):
        """
        Initializes a new instance of BaseModel class.
        Sets unique ID, creation timestamp, and update timestamp.
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        class_name = self.__class__.__name__
        return (f"[{class_name}] ({self.id}) {self.__dict__}")

    def save(self):
        """
        Updates the 'updated_at' attribute with the current timestamp.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Converts the BaseModel instance to a dictionary representation.
        Adds '__class__', 'created_at', and 'updated_at' keys.
        Returns the dictionary.
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
