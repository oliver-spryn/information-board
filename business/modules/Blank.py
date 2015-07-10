#!/usr/bin.python

from business.modules.ModuleBase import ModuleBase

class Blank(ModuleBase):
    """A no-op module.

    This module is intended for use on the first run after
    the device has been booted or started up again for the
    day. This blank display allows for any subsequent modules
    to prepare themselves for display after this one. This
    one, however, is simply blank and will make the display
    appear as though nothing is happening, while subsequent
    modules prepare themselves for display.
    """

    def draw_32(self):
        """Draw nothing on a 32x32 matrix.
        """
        pass

    def draw_64(self):
        """Draw nothing on a 64x32 matrix.
        """
        pass
