import unittest
from src.data_processor import SolarDataProcessor

class TestSolarDataProcessor(unittest.TestCase):
    def test_load_data_failure(self):
        processor = SolarDataProcessor("nonexistent.csv")
        self.assertFalse(processor.load_data())
        self.assertIsNone(processor.data)

    def test_profile_data_not_loaded(self):
        processor = SolarDataProcessor("dummy.csv")
        result = processor.profile_data()
        self.assertEqual(result, {"error": "Data not loaded"})

if __name__ == "__main__":
    unittest.main()