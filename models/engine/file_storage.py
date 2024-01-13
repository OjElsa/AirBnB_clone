#!/usr/bin/python3
"""serializes instances to JSON file and deserializes JSON file"""

import json
from models.base_model import BaseModel


class FileStorage:
    """Representation of a file data storage engine"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serialize _objects to the JSON file __file_path"""
        objf = FileStorage.__objects
        objdict = {obj: objf[obj].to_dict() for obj in objf.keys()}
        with open(FileStorage.__file_path, "w") as r:
            json.dump(objdict, r)

    def reload(self):
        """Deserialize the JSON file to __objects (only if file exists)."""
        try:
            with open(FileStorage.__file_path) as r:
                objdict = json.load(r)
                for o in objdict.values():
                    clsname = o["__class__"]
                    del o["__class__"]
                    cls = getattr(models, clsname)
                    self.new(cls(**o))
        except FileNotFoundError:
            return
