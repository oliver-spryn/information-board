#!/usr/bin/python

from exceptions import NotImplementedError
from models.parse.API import API

import json
import time
import urllib2

class ModuleBase(object):
    def __init__(self):
        self.duration = 0
        self.end_time = time.time()
        self.start_time = time.time()

    def draw(self):
        """Draw to the screen.

        This function is called on each draw request, but is
        implemented as a stub in this base class. If a child
        class does not override this function, and the application
        calls draw(), and excpetion will be thrown.

        Raises:
            NotImplementedError: An error caused by this function
                stub, since it needs overridden in order to
                implement the proper functionality.
        """
        raise NotImplementedError("ModuleBase.draw() must be overridden")

    def fetchAPIKey(self, name):
        row = API.Query.get(service = name)
        return row.key

    def fetchURL(self, url):
        """Fetch and parse an API call.

        Makes a call to an API and attempts to parse a JSON response
        into a generic Python dict.

        Args:
            url: The URL to the API.

        Returns:
            Either a dict, with the parsed results of the JSON response,
            or a string, if the response was not JSON.
        """
        contents = urllib2.urlopen(url).read()

        # Is this JSON?
        try:
            return json.loads(contents) # Yay
        except ValueError, e:
            pass                        # Nay

        # Is this XML?
            # Too bad!

        # Just return whatever text was given
        return contents
