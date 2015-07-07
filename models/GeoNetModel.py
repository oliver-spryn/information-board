#!/usr/bin/python

from models.ModelBase import ModelBase

class GeoNetModel(ModelBase):
    """Holds network and geolocation information.

    This model is designed to hold the user's network information,
    such as the public and LAN ip addresses, and the user's geo-
    location information, such as the latitude and longitude, as
    can be discovered by the network.

    Attributes:
        lan_ip: The user's LAN/local IP address.
        latitude: The latitude of the user.
        longitude: The longitude of the user.
        public_ip: The user's public IP address.
    """

    def __init__(self):
        self.lan_ip = ""
        self.latitude = 0.0
        self.longitude = 0.0
        self.public_ip = ""
