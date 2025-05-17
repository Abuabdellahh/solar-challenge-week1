from typing import Dict, Optional
import pandas as pd
from src.utils import load_data, generate_boxplot

class CrossCountryAnalyzer:
    """
    A class to handle cross-country comparison of solar data.

    Attributes:
        file_paths (Dict[str, str]): Dictionary of country names and file paths.
        datasets (Dict[str, pd.DataFrame]): Dictionary of country names and loaded DataFrames.
    """
    def __init__(self, file_paths: Dict[str, str]):
        """
        Initialize the analyzer with file paths for each country.

        Args:
            file_paths (Dict[str, str]): Dictionary of country names and file paths.
        """
        self.file_paths = file_paths
        self.datasets = {}

    def load_data(self) -> bool:
        """
        Load data for all countries and convert Timestamp to datetime.

        Returns:
            bool: True if all datasets are loaded successfully, False otherwise.
        """
        for country, path in self.file_paths.items():
            df = load_data(path)
            if df is not None:
                try:
                    df["Timestamp"] = pd.to_datetime(df["Timestamp"])
                    self.datasets[country] = df
                except Exception as e:
                    print(f"Error converting Timestamp for {country}: {e}")
                    return False
            else:
                print(f"Failed to load data for {country}")
                return False
        return True

    def plot_boxplot(self, column: str, save_path: Optional[str] = None) -> None:
        """
        Generate boxplot for a specified column across countries.

        Args:
            column (str): Column to plot.
            save_path (Optional[str]): Path to save plot.
        """
        if not self.datasets:
            print("No data loaded")
            return
        generate_boxplot(self.datasets, column, save_path)