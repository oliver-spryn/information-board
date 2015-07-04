#!/usr/bin/python

class Event(object):
    """The base class for all events.

    This class is the base class for all events used by this program,
    as it implements the complete observer pattern.

    Attributes:
        observers: A listing of all functions which will respond to
            this event.
    """

    def __init__(self):
        self.observers = list()

    def add_event_listener(self, listener):
        """Registers a handler function for this event.

        The "listener" parameter will be added to the listing of 
        observers which will respond to this event.

        Args:
            listener: A function which will respond to this event.
        """
        self.observers.append(listener)

    def dispatch_event(self, param = None):
        """Raises the event.

        All of the observers which are registered for this event are
        called and passed the "param" parameter.

        Args:
            param: An argument which is passed to each observer, 
                defaults to None.
        """

        for o in self.observers:
            o(param)