#!/usr/bin/python

import os
import socket
import time

from business.foundation.Queue import Queue
from business.modules.ModuleBase import ModuleBase
from business.parse.connection import register

# Register the Parse library with an account
app = os.environ.get("IB_PARSE_APP_ID")
key = os.environ.get("IB_PARSE_REST_API_KEY")
register(app, key)

import urllib2

def check_in():
    ext_ip = urllib2.urlopen('http://whatismyip.org').read()
    print ("Checking in from IP#: %s " % ext_ip)

check_in()

# http://api.hostip.info/get_json.php
# http://ipinfodb.com/ip_location_api.php
# http://labs.bible.org/api/?passage=votd&type=json&formatting=plain

# Get your public IP address
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8",80))
print(s.getsockname()[0])
s.close()

q = Queue()
mb = ModuleBase()
api = mb.fetchAPIKey("forecast.io")
#print mb.fetchURL("http://api.forecast.io/forecast/{0}/37.8267,-122.423".format(api.key))
