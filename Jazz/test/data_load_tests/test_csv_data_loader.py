
import unittest

from Jazz.src.data_load.csv_data_loader import CSVDataLoader


class TestCSVDataLoader(unittest.TestCase):
    def test_load_all_csv(self) -> None:
        dataLoader = CSVDataLoader()
        dataLoader.loadAllCSV("Jazz/test/data_load_tests/test_data")
        self.assertEqual(list(dataLoader.raw_data.keys()), ["test", "train"])
        self.assertEqual(dataLoader.raw_data["train"].shape, (891, 12))
        self.assertEqual(dataLoader.raw_data["test"].shape, (418, 11))