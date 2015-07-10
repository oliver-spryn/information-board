#!/usr/bin/python

from business.containers.LinkedList import LinkedList

class Queue(object):
    """The main display Queue.

    This class manages the Queue of objects which will render
    themselves on the display. It will manage keeping enough
    items in the Queue so that there will always be an item
    displaying on the screen. Additionally, once a registry
    of displayable items has been sent to this class, items
    will be chosen at random.

    Attributes:
        duration: The amount of time to display a single item
            on screen.
        list: The LinkedList object which will act as the main
            display queue.

    Args:
        duration: The amount of time to display a single item
            on screen.
        registry: A class containing a registry of objects
            which can be displayed on screen.
    """

    def __init__(self, duration):
        self.list = LinkedList()
        self.duration = duration

    def register(self, module):
        """Register a class as part of the Queue.

        This method will register the names of classes (not
        instances of a class) as part of the Queue for display.
        """

        self.list.append(module())

    def start(self):
        """Start running the Queue and the modules inside of it.
        """
        
        pass
