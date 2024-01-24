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
        return [instance for instance in storage.all().values() if isinstance
                (instance, cls)]
