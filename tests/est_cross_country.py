import unittest
from src.cross_country import CrossCountryAnalyzer

class TestCrossCountryAnalyzer(unittest.TestCase):
    def test_load_data_failure(self):
        analyzer = CrossCountryAnalyzer({"Test": "nonexistent.csv"})
        self.assertFalse(analyzer.load_data())
        self.assertEqual(len(analyzer.datasets), 0)

if __name__ == "__main__":
    unittest.main()