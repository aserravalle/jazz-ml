import os
import glob
import pathlib
import re
from typing import Dict, List
import pandas as pd

from Jazz.src.data_load.data_loader import DataLoader

class CSVDataLoader(DataLoader):

    def __init__(self, raw_data: Dict[str, pd.DataFrame] = {}):
        self.__raw_data = raw_data
    
    def loadCSV(self, filePath: str) -> None:
        p = pathlib.Path(filePath)
        assert p.suffix == ".csv", "File is not CSV"
        fileName = p.stem
        self.__raw_data[fileName] = pd.read_csv(filePath)
    
    def loadAllCSV(self, path: str) -> None:
        assert os.path.exists(path), "Path does not exist"
        for fileName in os.listdir(path):
            try:
                self.loadCSV(f"{path}/{fileName}")
            except AssertionError:
                continue

    def getRawData(self) -> Dict[str, pd.DataFrame]:
        return self.__raw_data

    