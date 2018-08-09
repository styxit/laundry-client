import os.path
import json

class ArgumentConfigLoader:

    # The loaded json config.
    config = None;

    def __init__(self, file):
        """Load and parse argument configuration from json.

        Parameters
        ----------
        file : string
            The base file name to load.
        """
        # Load json config from custom or default file.
        self.config = self.loadConfigFile(file)

    def list(self):
        """Get the parsed config as a list.

        Returns
        -------
        list
            The config as a list.

        """
        return self.config


    def loadConfigFile(self, file):
        """Load the custom or default config file as json.

        Parameters
        ----------
        file : string
            The filename as located in 'config'.

        Returns
        -------
        type
            Description of returned object.

        """
        defaultFile = 'config/' + file + '.json'
        customFile = "config/my." + file + '.json'

        if os.path.isfile(customFile):
            data = json.load(open(customFile))
        else:
            data = json.load(open(defaultFile))

        return data
