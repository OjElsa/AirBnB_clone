#!usr/bin/python3

""" A city class """

from models.base_model import BaseModel


class City(BaseModel):
    """ Represents a City

    Atrributes:
        state_id (str): State id
        city (str): name of the City
    """
    state_id = ""
    name = ""

    @classmethod
    def all(cls, storage):
        """Return a list of all instance of the class."""
        instances = storage.all().values()
        return [f"{instance} {instance.id}" for instance in instances if 
                isinstance(instance, cls)]
