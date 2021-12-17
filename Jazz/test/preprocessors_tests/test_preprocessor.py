
import unittest

import pandas as pd

from Jazz.src.preprocessors.preprocessor import Preprocessor


class TestPreprocessor(unittest.TestCase):
    def test_is_training(self) -> None:
        training_data = pd.DataFrame(columns=["id","x1", "x2","y"])
        self.assert_(self.PreprocessorForTest(raw_data=training_data).is_training())
        test_data = pd.DataFrame(columns=["id","x1", "x2"])
        self.assert_(not self.PreprocessorForTest(raw_data=test_data).is_training())

    def test_preprocess(self) -> None:
        training_data = pd.DataFrame(columns=["id","x1", "x2","y"])
        preprocessor = self.PreprocessorForTest(raw_data=training_data)
        preprocessor.run_preprocessing()
        self.assertEqual(preprocessor.logs, 
            "init\nrun_feature_engineering\nrun_one_hot_encoding\nrun_label_encoding\nrun_standard_scaler\n"
        )


    class PreprocessorForTest(Preprocessor):
        def __init__(self, raw_data):
            super().__init__(
                raw_data = raw_data,
                features = ["x1", "x2"],
                target = "y",
                identifier = "id"
            )
            self.logs = "init\n"
            self._clean_features = pd.DataFrame(columns=["x1", "x2"])


        def _run_feature_engineering(self) -> None:
            self.logs += "run_feature_engineering\n"

        def _run_one_hot_encoding(self) -> None:
            self.logs += "run_one_hot_encoding\n"

        def _run_label_encoding(self) -> None:
            self.logs += "run_label_encoding\n"

        def _run_standard_scaler(self) -> None:
            self.logs += "run_standard_scaler\n"
