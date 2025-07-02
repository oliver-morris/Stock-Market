import requests
from .Candlestick import Candlestick
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
    
    def stock_request(self, symbol, time_set="daily", full_output=True):
        # create an array to hold the Candlestick objects
        candlesticks = []
        
        # request the data input by user
        base_url = self.config["endpoints"]["time_series"]
        if full_output:
            base_url += "&outputsize=full"
        function = self.config["times"][time_set]
        url = base_url.format(function, symbol, self.api_key)
        r = requests.get(url)
        data = r.json()

        # ignore the meta data, only use candlestick data    
        key = list(data.keys())[1]
        data = data[key]

        # create the Candlestick objects and add to array
        for key, value in data.items():
            candlesticks.append(Candlestick(key, value))
        return candlesticks
    