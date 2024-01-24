#!usr/bin/python3

""" Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """ Represents the place Review

    Arttribute:
        place_id (str): Place Id
        user_id (str): User Id
        text (str): Text
    """
    place_id = ""
    user_id = ""
    text = ""

    @classmethod
    def all(cls, storage):
        """Return a list of all instances of the class."""
        return [instance for instance in storage.all().values() if isinstance
                (instance, cls)]
