import unittest
from src.utils import load_data

class TestUtils(unittest.TestCase):
    def test_load_data(self):
        self.assertIsNone(load_data("nonexistent.csv"))