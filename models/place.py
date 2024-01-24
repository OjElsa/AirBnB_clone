#!usr/bin/python3

""" Place Class"""

from models.base_model import BaseModel


class Place(BaseModel):
    """ Place Representation

    Attributes:
        city_id (str): City Id
        user_id (str): User Id
        name (str): Name of the place
        description (str): Description of the place
        number_rooms (int): Number of rooms in the place
        number_bathrooms (int): Number of bathrooms in the place
        max_guest (int): number of maximum guest in the place
        price_by_night (int): price of the place per night
        latitude (float): Latitude of the place
        longitude (float): Longitude of the Place
        amenity_ids (list): List of Amenity Ids
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    @classmethod
    def all(cls, storage):
        """Return a list of all instances of the class."""
        instances = storage.all().values()
        return [f"{instance} {instance.id}" for instance in instances if 
                isinstance(instance, cls)]
