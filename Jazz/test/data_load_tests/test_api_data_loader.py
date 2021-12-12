
import unittest

from Jazz.src.data_load.api_data_loader import APIDataLoader


class TestAPIDataLoader(unittest.TestCase):
    def test_get_from_api(self) -> None:
        dataLoader = APIDataLoader()
        dataLoader.loadFromJSON(data_name="people", endpoint="http://api.open-notify.org/astros.json")
        dataLoader.loadFromJSON(data_name="iss_position", endpoint="http://api.open-notify.org/iss-now.json")
        
        self.assertEqual(list(dataLoader.raw_data.keys()), ["people", "iss_position"])
        self.assertEqual(dataLoader.raw_data["people"].shape[1], 2)
        self.assertEqual(dataLoader.raw_data["iss_position"].shape[1], 2)
