#/usr/bin/python

from business.modules.ModuleBase import ModuleBase
from models.GeoNetModel import GeoNetModel

import json
import socket
import urllib2

class Forecast(ModuleBase):
    def __init__(self):
        self.api = self.fetchAPIKey("forecast.io")
        self.geo = self.discoverGeoNet()
        self.refreshData() 

    def discoverGeoNet(self):
        """Get your latitude & longitude.

        This methods uses your public IP address and a series of online
        services to discover the approximate latitude and longitude of
        your location for an accurate weather forecast.

        Returns:
            A model containing the user's public and LAN IP addresses
            and their geographic coordinates.
        """

        data = GeoNetModel()

        # Discover the public IP address
        addr = urllib2.urlopen("http://api.hostip.info/get_json.php").read()
        jaddr = json.loads(addr)
        data.public_ip = jaddr["ip"]

        # Discover the LAN IP address
#        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 #       s.connect(("8.8.8.8", 80))
  #      data.lan_ip = s.getsockname()[0]
   #     s.close()

        # Discover the latitude and longitude
        geo = urllib2.urlopen("http://freegeoip.net/json/{0}".format(data.public_ip)).read()
        jgeo = json.loads(geo)
        data.latitude = jgeo["latitude"]
        data.longitude = jgeo["longitude"]

        return data

    def refreshData(self):
        self.data = self.fetchURL("https://api.forecast.io/forecast/{0}/{1},{2}".format(self.api, self.geo.latitude, self.geo.longitude))
