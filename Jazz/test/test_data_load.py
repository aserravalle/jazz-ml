
import unittest
import os
print()
print()
print()
print()
print(os.getcwd())
from Jazz.src.data_load import DataLoad


class TestDataLoad(unittest.TestCase):
    def test_hello(self) -> None:
        dataLoad = DataLoad("Ariel")
        actual = dataLoad.hello()
        self.assertEqual(actual, "Ariel")
