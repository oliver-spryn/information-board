#!/usr/bin/python

from business.enums.Enum import Enum

class LayoutDirection(Enum):
    """Object orientation direction.

    The direction from the desired location which the object
    will be facing. For example, if the object is placed at
    the bottom-right of the screen, in order for the object
    to display on the screen, its direction will orient to
    the North West.

    Attributes:
        E: East
        N: North
        NE: North East
        NW: North West
        S: South
        SE: South East
        SW: South West
        W: West
    """

    E = 0
    N = 1
    NE = 2
    NW = 3
    S = 4
    SE = 5
    SW = 6
    W = 7
