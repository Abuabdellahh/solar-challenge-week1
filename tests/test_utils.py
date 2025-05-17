import unittest
import pandas as pd
from src.utils import load_data, compute_z_scores

class TestUtils(unittest.TestCase):
    def test_load_data(self):
        self.assertIsNone(load_data("nonexistent.csv"))
    
    def test_compute_z_scores(self):
        df = pd.DataFrame({"GHI": [100, 200, 300], "DNI": [50, 150, 250]})
        z_scores = compute_z_scores(df, ["GHI", "DNI"])
        self.assertIn("GHI_z", z_scores.columns)
        self.assertIn("DNI_z", z_scores.columns)
        self.assertAlmostEqual(z_scores["GHI_z"].mean(), 0, places=5)

if __name__ == "__main__":
    unittest.main()