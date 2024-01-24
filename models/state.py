#!usr/bin/python3

""" A state class"""

from models.base_model import BaseModel


class State(BaseModel):
    """ Represents a state

    Attributes:
        state (str): Name of State
    """
    name = ""

    @classmethod
    def all(cls, storage):
        """Return a list of all instances of the class."""
        instances = storage.all().values()
        return [f"{instance} {instance.id}" for instance in instances if 
                isinstance(instance, cls)]
