#!/usr/bin/python

from business.exceptions.FirebaseSecretMissingException import FirebaseSecretMissingException
from business.exceptions.FirebaseAuthInvalidException import FirebaseAuthInvalidException

from firebase import firebase

import os

class FirebaseFactory:
    """Firebase connector object.

    This factory allows the programmer to bypass the step
    of authenticating with Firebase before using the API.
    All of the authentication is handled internally before
    releasing Firebase Python interface for use in the rest
    of the program.

    Args:
        URL: The URL to the Firebase dataset.

    Raises:
        FirebaseSecretMissingException: Thrown whenever the
            IB_FIREBASE_SECRET environment variable is not
            set.

    Returns:
        A Firebase API object with authenticaion already
        applied.
    """

    def __new__(cls, URL):
    # Get the Firebase API key
        secret = os.environ.get("IB_FIREBASE_SECRET")

        if secret is None:
            raise FirebaseSecretMissingException("The environment variable IB_FIREBASE_SECRET cannot be found.")

    # Create the authentication
        # Per: https://github.com/ozgur/python-firebase/blob/master/firebase/firebase.py#L172
        # the second parameter is really not even used
        auth = firebase.FirebaseAuthentication(secret, None)

    # Set up Firebase
        fb = firebase.FirebaseApplication(URL, auth)

        if fb.get("/", None) is None:
            raise FirebaseAuthInvalidException("The API key used to connect to the Firebase API is invalid.")

        return fb
