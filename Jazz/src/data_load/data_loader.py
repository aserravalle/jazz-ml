from abc import ABC
from typing import Dict
import pandas as pd

class DataLoader(ABC):
    @property                 
    def raw_data(self) -> Dict[str, pd.DataFrame]:     
        return self._raw_data
