import requests
import json
import os
import tomli

class Requests:
    def __init__(self, api_key):
        self.api_key = api_key
        self.config = self.__load_config()

    @staticmethod
    def __load_config():
        # get the path of the config file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(current_dir, '..'))
        config_path = os.path.join(project_root, 'config.toml')

        # return config file
        with open(config_path, 'rb') as f:
            config = tomli.load(f)
        return config