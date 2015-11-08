#!/usr/bin/python

from business.exceptions.logentry.LogTypeUnavailableException import LogTypeUnavailableException
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
        log.setLevel(cls.to_log_level(level))
        log.addHandler(LogentriesHandler(key))

        return log

    def to_log_level(level):
        """Translates a string to a Python log enum.

        Logentry configuration values are stored in the
        database as string values. This method will
        translate these values to Python log enum.

        Raises:
            LogTypeUnavailableException: Thrown whenever
                the requested log type does not map to
                an available logging level.

        Returns:
            A Python log enum value.
        """

        logs = {
            "critital"    : logging.CRITICAL,
            "crit"        : logging.CRITICAL,
            "emergency"   : logging.CRITICAL,
            "emerg"       : logging.CRITICAL,
            "alert"       : logging.CRITICAL,

            "error"       : logging.ERROR,
            "err"         : logging.ERROR,

            "warning"     : logging.WARNING,
            "warn"        : logging.WARNING,

            "information" : logging.INFO,
            "info"        : logging.INFO,
            "notice"      : logging.INFO,
            "note"        : logging.INFO,

            "debugging"   : logging.DEBUG,
            "debug"       : logging.DEBUG,

            "notset"      : logging.NOTSET
        }

        if level in logs:
            return logs[level]
        else:
            raise LogTypeUnavailableException("'{0}' does not map to an available logging level.".format(level))
