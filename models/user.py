#!usr/bin/python3

"""User Class"""

from models.base_model import BaseModel


class User(BaseModel):
    """ Represents a User

    Attributes:
        email (str): Email of User
        password (str): Password of user
        first_name (str): First Name of the user
        last_name (str): Last Name of the user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    @classmethod
    def all(cls, storage):
        """Return a list of all instances of the class."""
        return [instance for instance in storage.all().values() if isinstance
                (instance, cls)]
