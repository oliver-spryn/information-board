#!/usr/bin/python

from business.exceptions.Exception import Exception

class URLMissingException(Exception):
    """No Firebase URL can be found.

    Thrown whenever the application cannot find an
    environment variable called IB_FIREBASE_URL
    which holds the URL to Firebase.

    Args:
        msg: The exception message
    """

    def __init__(self, msg):
        super(URLMissingException, self).__init__(msg)
