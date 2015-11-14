#!/usr/bin/python

from abc import ABCMeta, abstractmethod
from business.factories.LogentryFactory import LogentryFactory

import os

# Use actual drivers on RPi and mocks on all other hardware
rpi = os.environ.get("IB_TARGET_HARDWARE")

if rpi is None:
    pass
else:
    pass

class Viewer(metaclass = ABCMeta):
    """The base viewer class.

    All of the basic functionality to draw pixels onto
    the display is provided by this class. Access to the
    low-level drivers and hardware information is provided
    by this class, as well as helpers to aid in the
    drawing of information to various matrix sizes.
    """

    def __init__(self):
        pass
