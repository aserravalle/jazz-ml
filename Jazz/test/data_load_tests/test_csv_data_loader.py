
import unittest

from Jazz.src.data_load.csv_data_loader import CSVDataLoader


class TestCSVDataLoader(unittest.TestCase):
    def test_load_all_csv(self) -> None:
        dataLoader = CSVDataLoader()
        dataLoader.loadAllCSV("Jazz/assets/data")
        raw_data = dataLoader.getRawData()
        self.assertEqual(list(raw_data.keys()), ["test", "train"])
        self.assertEqual(raw_data["train"].shape, (891, 12))
        self.assertEqual(raw_data["test"].shape, (418, 11))
