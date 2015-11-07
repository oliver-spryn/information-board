#!/usr/bin/python

from business.exceptions.firebase.AuthInvalidException import AuthInvalidException
from business.exceptions.firebase.SecretMissingException import SecretMissingException
from business.exceptions.firebase.URLMissingException import URLMissingException

from firebase import firebase

import os

class FirebaseFactory:
    """Firebase connector object.

    This factory allows the programmer to bypass the step
    of authenticating with Firebase before using the API.
    All of the authentication is handled internally before
    releasing Firebase Python interface for use in the rest
    of the program.

    Raises:
        AuthInvalidException: Thrown whenever the API key or
            the connection URL is invalid and the application
            is not granted access to the Firebase data set.
        SecretMissingException: Thrown whenever the
            IB_FIREBASE_SECRET environment variable is not
            set.
        URLMissingException: Thrown whenever the
            IB_FIREBASE_URL environment variable is not
            set.

    Returns:
        A Firebase API object with authenticaion already
        applied.
    """

    def __new__(cls):
    # Get the Firebase URL and API key
        secret = os.environ.get("IB_FIREBASE_SECRET")
        url = os.environ.get("IB_FIREBASE_URL")

        if secret is None:
            raise SecretMissingException("The environment variable IB_FIREBASE_SECRET cannot be found.")

        if url is None:
            raise URLMissingException("The environment variable IB_FIREBASE_URL cannot be found.")

    # Create the authentication
        # Per: https://github.com/ozgur/python-firebase/blob/master/firebase/firebase.py#L172
        # the second parameter is really not even used
        auth = firebase.FirebaseAuthentication(secret, None)

    # Set up Firebase
        fb = firebase.FirebaseApplication(url, auth)

        if fb.get("/", None) is None:
            raise AuthInvalidException("The URL or API key used to connect to the Firebase API is invalid.")

        return fb
