#!usr/bin/python3

""" A state class"""

from models.base_model import BaseModel


class State(BaseModel):
    """ Represents a state

    Attributes:
        state (str): Name of State
    """
    name = ""
