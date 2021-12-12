from abc import ABC, abstractmethod
from typing import Dict
import pandas as pd

class DataLoader(ABC):
    __raw_data = {}

    def getRawData(self) -> Dict[str, pd.DataFrame]:
        return self.__raw_data