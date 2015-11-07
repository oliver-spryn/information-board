#!/usr/bin/python

from business.exceptions.Exception import Exception

class SecretMissingException(Exception):
    """No Firebase secret can be found.

    Thrown whenever the application cannot find an
    environment variable called IB_FIREBASE_SECRET
    which holds the API key to Firebase.

    Args:
        msg: The exception message
    """

    def __init__(self, msg):
        super(SecretMissingException, self).__init__(msg)
