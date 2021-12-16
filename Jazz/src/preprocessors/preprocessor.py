from abc import ABC, abstractmethod
from typing import Dict, List
import pandas as pd

class Preprocessor(ABC):
    @property
    def raw_data(self) -> Dict[str, pd.DataFrame]:     
        return self._raw_data

    @property
    def features(self) -> List[str]:     
        return self._features

    @property
    def X(self) -> pd.DataFrame:
        return self._raw_data
