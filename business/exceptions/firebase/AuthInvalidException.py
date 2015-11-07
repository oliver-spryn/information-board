#!/usr/bin/python

from business.exceptions.Exception import Exception

class AuthInvalidException(Exception):
    """Firebase authentication is invalid.

    Thrown whenever the API key used to log into the
    Firebase API is invalid.

    Args:
        msg: The exception message
    """

    def __init__(self, msg):
        super(AuthInvalidException, self).__init__(msg)
