#!usr/bin/python3

""" Review class"""

from models.base_model import baseModel


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
