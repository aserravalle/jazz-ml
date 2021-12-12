import os
from typing import Dict
import pandas as pd
import json
import urllib.request

from Jazz.src.data_load.data_loader import DataLoader

class APIDataLoader(DataLoader):

    def __init__(self, raw_data: Dict[str, pd.DataFrame] = {}):
        self._raw_data = raw_data
    
    def get(self, endpoint: str) -> Dict:
        file = urllib.request.urlopen(endpoint)
        data = json.loads(file.read())
        print(type(data))
        return data

    def loadFromJSON(self, data_name: str, endpoint: str) -> None:
        data = self.get(endpoint)
        if type(data[data_name]) == list:
            self._raw_data[data_name] = pd.io.json.json_normalize(data[data_name])
        else:
            self._raw_data[data_name] = pd.DataFrame(data[data_name], index=[0])
    