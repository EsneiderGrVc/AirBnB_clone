#!/usr/bin/python3
from models.base_model import BaseModel


class Place(BaseModel):
    """
    This class inherits from base models
    eleven public attributes are created
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = ""
    number_bathrooms = ""
    max_guest = ""
    price_by_night = ""
    latitude = ""
    longitude = ""
    amenity_ids = ""
