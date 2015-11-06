#!/usr/bin/python

import os

class Bootstrapper:
    """The class which kickstarts the queue.

    The bootstrapper creates the initial connection to the
    Firebase application to identify which plugins should be
    loaded and which plugin will act as the 'core' plugin to
    load only once during initialization.

    Attributes:
        fbSecret: The Firebase API secret key for
            authentication purposes
    """

    def __init__(self):
    
