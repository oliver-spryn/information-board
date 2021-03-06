#!/usr/bin/python

from exceptions import NotImplementedError
from models.ModuleDataModel import ModuleDataModel
from models.parse.API import API

import json
import time
import urllib2

class ModuleBase(object):
    """The base class for all modules.

    This class defines some basic functionality which is common to
    all modules in this project. It also holds and processes some
    information which each module may needs to access, as well as
    define an interface which the implementation of each module
    will require.

    Attributes:
        data: A model containing several pieces of information which
            is common to all modules.

    Args:
        duration: The amount of time for which this module will be on
            display.
        start_time: The time at which the module will start displaying
            next.
        end_time: The time at which the module will stop displaying
            next.
    """

    def __init__(self, duration, start_time, end_time):
        self.data = ModuleDataModel()
        self.data.duration = duration
        self.data.start_time = start_time
        self.data.end_time = end_time

    def draw_32(self):
        """Draw to a 32x32 matrix.

        This function is called on each draw request, but is
        implemented as a stub in this base class. If a child
        class does not override this function, and the application
        calls this function, an excpetion will be thrown.

        Raises:
            NotImplementedError: An error caused by this function
                stub, since it needs overridden in order to
                implement the proper functionality.
        """
        raise NotImplementedError("ModuleBase.draw_32() must be overridden")

    def draw_64(self):
        """Draw to a 64x32 matrix.

        This function is called on each draw request, but is
        implemented as a stub in this base class. If a child
        class does not override this function, and the application
        calls this function, an excpetion will be thrown.

        Raises:
            NotImplementedError: An error caused by this function
                stub, since it needs overridden in order to
                implement the proper functionality.
        """
        raise NotImplementedError("ModuleBase.draw_64() must be overridden")

    def fetch_api_key(self, name):
        row = API.Query.get(service = name)
        return row.key

    def fetch_url(self, url):
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

    def module_end(self, next_start, next_end):
        """Called when this module has finished its display.

        This method allows for any clean-up or updates which may be
        needed after a module has finished its display.

        Args:
            next_start: The time at which this module will be called
                next time.
            next_end: The time at which this module will finish next
                time.
        """

        self.data.displaying_now = False
        self.data.last_time = self.data.end_time
        self.data.start_time = start_time
        self.data.end_time = end_time

    def module_next(self):
        """Called when this module is next in line.

        Allows a module to perform any pre-processing which may be
        necessary before it is displayed on-screen. It is not
        required to override this function, if no pre-processing is
        needed.
        """
        pass

    def module_start(self):
        """Last-chance preparations before display.

        Called immediately before the first request to the drawing
        function in order to allow for any last preparations before
        display on-screen. It is not required to override this
        function, if no pre-processing is needed.
        """

        self.data.display_count += 1
        self.data.displayed_yet = True
        self.data.displaying_now = True
