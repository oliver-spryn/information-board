#!/usr/bin/python

from enums.LayoutDirection import LayoutDirection
from models.ModelBase import ModelBase
from models.PointModel import PointModel

class LayoutLocationModel(ModelBase):
    """The location of an on-screen object.

    This model holds the point at which an object will be
    placed on screen, as determined by the Layout class.
    It will also hold additional metadata, such as a
    boolean to determine whether or not an object will fit
    on the screen, given these dimensions.

    Attributes:
        direction: The direction from the desired location at
            which the object will be facing. For example, if
            the object is placed at the bottom-right of the
            screen, in order for the object to display on the
            screen, its direction will orient to the North
            West.
        location: The location of the object.
        on_screen: Whether or not the object will fit on
            the matrix.
    """

    direction = LayoutDirection()
    location = PointModel()
    on_screen = False
