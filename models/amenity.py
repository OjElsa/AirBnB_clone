#!usr/bin/python3

""" Amenity Class"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents Amenity

    Attributes:
        name (str): Name of Amenity
    """
    name = ""

    @classmethod
    def all(cls, storage):
        """Return a list of all instances of the class"""
        instances = storage.all().values()
        return [f"{instance} {instance.id}" for instance in instances if isinstance(instance, cls)]
