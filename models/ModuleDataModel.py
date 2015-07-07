#!/usr/bin/python

from models.ModelBase import ModelBase
from time import time

class ModuleDataModel(ModelBase):
    """Common data stored for all modules.

    In order for a module to presist within the Queue, some
    state information should be retained. This model contains
    the most important information which should be retained
    for use whenever the Queue runs a particular module again.

    Attributes:
        display_count: The number of times this module has been
            displayed.
        displayed_yet: Whether or not this module has been
            displayed yet.
        displaying_now: Whether or not this module is currently
            displaying.
        duration: The number of seconds for which this module
            will be displayed on-screen.
        end_time: The time at which this module will finish
            its display next.
        last_time: The time at which the last display finished.
        start_time: The time at which this module will be
            displayed next.
    """

    def __init__(self):
        self.display_count = 0
        self.displayed_yet = False
        self.displaying_now = False
        self.duration = 0
        self.end_time = time()
        self.last_time = time()
        self.start_time = time()
