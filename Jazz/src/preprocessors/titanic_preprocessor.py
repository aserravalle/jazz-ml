import numpy as np
import pandas as pd

from Jazz.src.preprocessors.preprocessor import Preprocessor


class TitanicPreprocessor(Preprocessor):

#region Field Names
    OHE_COLUMNS = ["Embarked"]
    LE_COLUMNS = ["Ticket", "Cabin"]
    TARGET = "Survived"
    ID = "PassengerId"
    FEATURES_RAW = [
        "Pclass",
        "Sex",
        "Age",
        "SibSp",
        "Parch",
        "Ticket",
        "Fare",
        "Cabin",
        "Embarked",
    ]
    FEATURES_PREPROCESSED = [
        "Pclass",
        "Sex",
        "Age",
        "SibSp",
        "Parch",
        "Ticket",
        "Fare",
        "Cabin",
        "Embarked_Cherbourg",
        "Embarked_Queenstown",
        "Embarked_Southampton",
    ]
#endregion

    def __init__(self, raw_data):
        super().__init__(
            raw_data = raw_data,
            features = self.FEATURES_PREPROCESSED,
            target = self.TARGET,
            identifier = self.ID
        )
        self.clean_features = raw_data[self.FEATURES_RAW].copy()
        # self.encoders = Encoders(model_folder_name, training) # TODO: Add encoders

    def _run_feature_engineering(self) -> None:
        print("Feature engineering")
        self.clean_features["Sex"] = np.where(
            self.clean_features["Sex"] == self.clean_features["Sex"].mode().iloc[0], 1, 0
        )
        self.clean_features["Embarked"] = self.clean_features["Embarked"].fillna(
            self.clean_features["Embarked"].mode().iloc[0]
        )
        self.clean_features["Age"] = self.clean_features["Age"].fillna(self.clean_features["Age"].mean())
        self.clean_features["Cabin"] = self.clean_features["Cabin"].fillna("Unknown")
        self.clean_features["Embarked"] = self.clean_features["Embarked"].map(
            {"C": "Cherbourg", "Q": "Queenstown", "S": "Southampton"}
        )

    def _run_one_hot_encoding(self) -> None:
        print("One-hot encode small categorical variables")
        for col in self.OHE_COLUMNS:
            df_to_encode = self.clean_features[[col]]
            # ohe_df = self.encoders.fit_transform_ohe(df_to_encode,col,"titanic") # TODO: Encoders
            self.clean_features = pd.concat([self.clean_features.drop([col], axis=1), ohe_df], axis=1)

    def _run_label_encoding(self) -> None:
        print("Label encode large categorical variables")
        for col in self.LE_COLUMNS:
            series_to_encode = self.clean_features[col]
            self.clean_features[col] = self.encoders.fit_transform_le(series_to_encode,col,"titanic")

    def _run_standard_scaler(self) -> None:
        print("Standardise numerical features")
        features = list(self.clean_features.columns)
        self.clean_features = self.encoders.fit_transform_standardise(
            data=self.clean_features,
            features=features
        )
        self.clean_features = self.clean_features.apply(inf_to_nan).fillna(-99)
