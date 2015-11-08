#!/usr/bin/python

from business.exceptions.Exception import Exception

class LogTypeUnavailableException(Exception):
    """Requested log type is invalid.

    Thrown whenever the logging type in Firebase does
    not map to an available logging level.

    Args:
        msg: The exception message
    """

    def __init__(self, msg):
        super(LogTypeUnavailableException, self).__init__(msg)
