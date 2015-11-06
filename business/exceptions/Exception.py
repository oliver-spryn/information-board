#!/usr/bin/python

class Exception:
    """The base exception class.

    All exceptions which will be thrown by this project
    are derived from this class.

    Attributes:
        message: The exception message.

    Args:
        msg: The exception message.
    """

    def __init__(self, msg):
        self.message = msg

    def getMessage(self):
        """Gets the exception message.

        Returns:
            The exception message.
        """

        return self.message
