import unittest
import pandas as pd
from src.utils import load_data, compute_z_scores, impute_missing_values

class TestUtils(unittest.TestCase):
    def test_load_data(self):
        self.assertIsNone(load_data("nonexistent.csv"))
    
    def test_compute_z_scores(self):
        df = pd.DataFrame({"GHI": [100, 200, 300], "DNI": [50, 150, 250]})
        z_scores = compute_z_scores(df, ["GHI", "DNI"])
        self.assertIn("GHI_z", z_scores.columns)
        self.assertIn("DNI_z", z_scores.columns)
        self.assertAlmostEqual(z_scores["GHI_z"].mean(), 0, places=5)
    
    def test_impute_missing_values(self):
        df = pd.DataFrame({"GHI": [100, None, 300], "DNI": [50, 150, None]})
        imputed = impute_missing_values(df, ["GHI", "DNI"])
        self.assertFalse(imputed["GHI"].isna().any())
        self.assertFalse(imputed["DNI"].isna().any())
        self.assertEqual(imputed["GHI"][1], 200)  # Median of [100, 300]

def test_placeholder():
    assert True

if __name__ == "__main__":
    unittest.main()