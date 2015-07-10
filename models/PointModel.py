#!/usr/bin/python

from models.ModelBase import ModelBase

class PointModel(ModelBase):
    """Holds the X, Y location of an object.

    Attributes:
        x: The X location of an object.
        y: The Y location of an object.
    """

    x = 0
    y = 0
