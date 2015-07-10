#!/usr/bin/python

class ModuleCollection(ModuleBase):
    """A container for multiple modules.

    Some modules are best displayed as a collection of screens,
    much like a slideshow presentation. This prevents a single
    module from having to compress too much information onto a
    small screen, by spreading out its content over multiple
    screens. This class will help those modules achieve that
    goal, to display their screens in order, within the amount
    of time given by the main Queue.

    Attributes:
        instances: A list of modules which will be displayed as
            part of this collection.
        unit_duration: The amount of time for which an individual
            module will be on display.

    Args:
        duration: The amount of time for which this module
            collection will be on display.
        start_time: The time at which the module will start
            displaying next.
        end_time: The time at which the module will stop
            displaying next.
    """

    def __init__(self, duration, start_time, end_time):
        super(ModuleCollection, self).__init__(duration, start_time, end_time)
        self.instances = []
        self.unit_duration = duration

    def draw_32(self):
        pass

    def draw_64(self):
        pass

    def module_next(self):
        """Propigates the event call to the first registered module.
        """

        if len(self.instances) > 0:
            self.instances[0].module_next()

    def register(self, module):
        """Register a class as part of the collection.

        This method will register the names of classes (not
        instances of a class) as part of the module collection
        for display.
        """

        self.registry.append(module())
        self.unit_duration = self.data.duration / len(self.registry)
