#!/usr/bin/python

from abc import ABCMeta, abstractmethod

class Controller(metaclass = ABCMeta):
    """The base controller class.

    This class provides much of the common functionality which
    the plugin controllers will need, such as fetching the
    settings and making network operations.

    Attributes:
        name: The plugin's name
        fb: The Firebase factory object
        log: The Logentry factory object
    """

    def __init__(self, name, fb, log):
        self.name = name
        self.fb = fb
        self.log = log

        self.log.info("Initializing the {0} plugin".format(self.name))
