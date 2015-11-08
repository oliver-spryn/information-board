#!/usr/bin/python

from business.foundation.Moderator import Moderator

class Bootstrapper:
    """The class which kickstarts the queue.

    The bootstrapper creates the initial connection to the
    Firebase application to identify which plugins should be
    loaded and which plugin will act as the 'core' plugin to
    load only once during initialization.

    Attributes:
        fb: The Firebase factory object
        log: The Logentry factory object
    """

    def __init__(self, fb, log):
        self.fb = fb
        self.log = log
        self.mod = Moderator(10)
        self.log.info("Bootstrapping the plugin queue.")

        self.get_start_plugin()
        self.get_plugin_list()

    def get_plugin_list(self):
        """Returns a list of plugins.

        --- Blocking I/O operation ---

        A query is sent to Firebase which returns a list of
        all plugins which are installed in the database. This
        list is formatted as a Python array.

        Returns:
            A list of installed plugins.
        """

        # Applied workaround for issue 19
        # https://github.com/ozgur/python-firebase/issues/19#issuecomment-39660298
        self.log.info("Fetching the list of installed plugins.")
        plugins = self.fb.get("/plugins", name = None, params = { "shallow": "true" })
        self.log.info("Found {0} plugins(s).".format(len(plugins)))

        return list(plugins)

    def get_start_plugin(self):
        """Get the name of the plugin to show during
        initialization.

        --- Blocking I/O operation ---

        This methods makes a call to Firebase to fetch the name
        of the plugin which is intended to show during the
        initialization of this program.

        Returns:
            The of the plugin to display during the
            initialization phase.
        """
        self.log.info("Fetching the name of the initialization plugin.")
        init = self.fb.get("/init", None)
        self.log.info("Got the initialization plugin: {0}.".format(init["plugin"]))

        return init["plugin"]
