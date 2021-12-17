from abc import ABC, abstractmethod
from typing import Dict, List
import pandas as pd

class Preprocessor(ABC):

#region Data properties

    @property
    def features(self) -> List[str]:     
        return self._features
        
    @property
    def target(self) -> str:
        return self._target

    @property
    def identifier(self) -> str:
        return self._identifier

    @property
    def non_features(self) -> List[str]:
        if self.is_training():
            return [self._identifier, self._target]
        else:
            return [self._identifier]

    @property
    def raw_data(self) -> Dict[str, pd.DataFrame]:     
        return self._raw_data

    @property
    def clean_data(self) -> pd.DataFrame:
        """
        Clean data frame with id, features, and target variables for training data
        """
        return pd.concat([
                self.raw_data[self.non_features], self.clean_features
            ], axis=1)


    @property
    def clean_features(self) -> pd.DataFrame:
        """
        Clean data frame with id, features, and target variables for training data
        """
        return self._clean_features

#endregion

    @abstractmethod
    def __init__(
            self,
            raw_data: Dict[str, pd.DataFrame],
            features: List[str],
            target: str,
            identifier: str,
        ):
        self._raw_data = raw_data
        self._features = features
        self._target = target
        self._identifier = identifier

    def is_training(self) -> bool:
        return self.raw_data.columns.__contains__(self._target)

    def run_preprocessing(self) -> pd.DataFrame:
        data_type = "training" if self.is_training() else "prediction"
        print(f"Preprocessing {data_type} data")

        self._run_feature_engineering()
        self._run_one_hot_encoding()
        self._run_label_encoding()
        self._run_standard_scaler()
        
        # self.encoders.save_encoders()

        print(f"Returning preprocessed {data_type} data")

        return self.clean_data

    @abstractmethod
    def _run_feature_engineering(self) -> None:
        pass

    @abstractmethod
    def _run_one_hot_encoding(self) -> None:
        pass

    @abstractmethod
    def _run_label_encoding(self) -> None:
        pass

    @abstractmethod
    def _run_standard_scaler(self) -> None:
        pass
