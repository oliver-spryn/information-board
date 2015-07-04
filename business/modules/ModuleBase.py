#!/usr/bin/python

from exceptions import NotImplementedError
import time

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

    def fetchAPIKey(self):
        pass
