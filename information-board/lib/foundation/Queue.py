#!/usr/bin/python

from containers.LinkedList import LinkedList

class Queue(object):
    """The main display Queue.

    This class manages the Queue of objects which will render
    themselves on the display. It will manage keeping enough
    items in the Queue so that there will always be an item
    displaying on the screen. Additionally, once a registry
    of displayable items has been sent to this class, items
    will be chosen at random.

    Args:
        registry: A class containing a registry of objects
            which can be displayed on screen.
        time: The amount of time to display a single item
            on screen.

    Attributes:
        list: The LinkedList object which will act as the main
            display queue.
    """

    def __init__(self):
        self.list = LinkedList()
