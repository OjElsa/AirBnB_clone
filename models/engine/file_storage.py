#!/usr/bin/python3
"""serializes instances to JSON file and deserializes JSON file"""

import json
import inspect
from models import base_model
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Representation of a file data storage engine"""
    __file_path = "file.json"
    __objects = {}
    _valid_classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Place": Place,
            "Amenity": Amenity,
            "Review": Review
    }

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
                    if clsname in self._valid_classes:
                        self.new(eval(clsname)(**o))
        except FileNotFoundError:
            return

    def classes(self):
        """Return a dictionary of class names mapped to class objects."""
        return {name: cls for name, cls in inspect.getmembers(base_model,
                inspect.isclass)}
