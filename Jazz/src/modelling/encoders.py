import bisect
from typing import Dict, List
import numpy as np
import os
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler


class Encoders:
    def __init__(self, model_folder_name: str, training: bool):
        self.model_folder_name = model_folder_name
        self.training = training
        self.encoders_dic = self.load_encoders_if_predicting(training, model_folder_name)

    def load_encoders_if_predicting(self, training: bool, model_folder_name: str) -> Dict[str, object]:
        if not training:
            encoders_path = get_model_folder_path(model_folder_name)
            encoders_dic = self._read_pkl_files_in_directory(encoders_path)
        return encoders_dic

    def _read_pkl_files_in_directory(self, encoders_path: str) -> Dict[str, object]:
        print(f"Loading encoders from {encoders_path}")
        encoders_dic = {}
        for file_name_ext in os.listdir(encoders_path):
            file_path = f"{encoders_path}/{file_name_ext}"
            file_name, ext = file_name_ext.split(".")
            if ext == "pkl":
                encoders_dic[file_name] = read_pkl(file_path)
        return encoders_dic
                    
    def save_encoders(self) -> None:
        self.save_encoders_if_training(
            model_folder_name=self.model_folder_name,
            training=self.training,
            encoders_dic=self.encoders_dic,
        )
        
    def save_encoders_if_training(self, model_folder_name:str, training:bool, encoders_dic:Dict[str,object]) -> None:
        print(f"saving encoders: {training}")
        if training:
            for key in encoders_dic.keys():
                save_new_pkl_object(model_folder_name, key, encoders_dic[key])


    def fit_transform_ohe(self, data:pd.DataFrame, col_name:str, table_name:str) -> pd.DataFrame:
        ohe_col_name = f"ohe_{col_name}_{table_name}"
        if self.training:
            self.encoders_dic[ohe_col_name] = OneHotEncoder(handle_unknown="ignore").fit(data)
        ohe_features = self.encoders_dic[ohe_col_name].get_feature_names([col_name])
        ohe_df = pd.DataFrame(
            self.encoders_dic[ohe_col_name].transform(data.values).toarray(),
            columns=[f for f in ohe_features]
        )
        return ohe_df

    
    def fit_transform_le(self, data:pd.Series, col_name:str, table_name:str) -> pd.Series:
        le_col_name = f"le_{col_name}_{table_name}"
        if self.training:
            le = LabelEncoder().fit(data)
            le_classes = le.classes_.tolist()
            bisect.insort_left(le_classes, '<unknown>')
            le.classes_ = le_classes
            self.encoders_dic[le_col_name] = le
        data_declassified = np.where(
            data.isin(self.encoders_dic[le_col_name].classes_),
            data,
            "<unknown>",
        )
        return pd.Series(self.encoders_dic[le_col_name].transform(data_declassified))


    def fit_transform_standardise(self, data:pd.DataFrame, features: List[str]) -> pd.DataFrame:
        if self.training:
            self.encoders_dic["scaler"] = StandardScaler().fit(data)
        return pd.DataFrame(
            self.encoders_dic["scaler"].transform(data), columns=features
        )