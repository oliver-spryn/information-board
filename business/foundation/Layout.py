#!/usr/bin/python

from models.PointModel import PointModel

class Layout(object):
    """Class for object placement.

    Measures and calculates how to place an object on the
    display in order to fit in variou,s requested locations.

    Attributes:
        height: The matrix height.
        width: The matrix width.

    Args:
        width: The matrix width.
        height: The matrix height.
    """

    def __init__(self, width, height):
        self.height = height
        self.width = width

    def top_left(self, width, height):
        """Place the object in the top left.

        Args:
            width: The width of the object being placed.
            Height: The height of the object being placed.

        Returns:
            The X, Y coordinates at which the object should be
            placed.
        """

        pm = PointModel()
        pm.x = 0
        pm.y = 0
        return pm
