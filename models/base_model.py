#!/usr/bin/python3
""" Defines all common arttributes/methods for orther classes """

from uuid import uuid4
from datetime import datetime

class BaseModel():
    """"BaseModel class"""
    def __init__(self):
        """Intialize a new BaseModel class"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """return the representstion string of the BaseModel instance"""
        className = self.__class__.__name__
        return ("[{}] ({}) {})".format(className, self.id, self.__dict__))

    def save(self):
        """updates public instance attribute updated_at with current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ return a dictionary containing all keys/values of the instance"""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
