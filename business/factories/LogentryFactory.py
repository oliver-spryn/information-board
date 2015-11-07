#!/usr/bin/python

from logentries import LogentriesHandler
import logging

class LogentryFactory:
    """Logentry connector object.

    This factory imports the API key, log set name, and
    log level from Firebase to configure the Logentry
    instance for application logging.

    Args:
        fb: A FirebaseFactory instance.

    Returns:
        A Logentry API object with authentication already
        applied.
    """

    def __new__(cls, fb):
    # Obtain the configuration from Firebase
        config = fb.get("/logging", None)
        level = config['report_level']
        key = config['key']

    # Connect to Logentry and configure the log level
        log = logging.getLogger("logentries")
        log.setLevel(logging.WARN)
        log.addHandler(LogentriesHandler(key))

        return log
