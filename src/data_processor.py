from typing import Optional, List
import pandas as pd
from src.utils import load_data, compute_z_scores, plot_time_series

class SolarDataProcessor:
    """
    A class to handle solar data processing tasks including loading, profiling, cleaning, and visualization.

    Attributes:
        file_path (str): Path to the CSV file.
        data (pd.DataFrame): Loaded DataFrame.
    """
    def __init__(self, file_path: str):
        """
        Initialize the processor with a file path.

        Args:
            file_path (str): Path to the CSV file.
        """
        self.file_path = file_path
        self.data = None

    def load_data(self) -> bool:
        """
        Load data from CSV file.

        Returns:
            bool: True if successful, False otherwise.
        """
        self.data = load_data(self.file_path)
        if self.data is not None:
            self.data["Timestamp"] = pd.to_datetime(self.data["Timestamp"])
            return True
        return False

    def profile_data(self) -> dict:
        """
        Generate summary statistics, missing values, and validation checks.

        Returns:
            dict: Profiling results including statistics, missing values, and negative GHI count.
        """
        if self.data is None:
            return {"error": "Data not loaded"}
        
        key_columns = ["GHI", "DNI", "DHI", "ModA", "ModB", "WS", "WSgust", "Tamb", "RH", "BP"]
        stats = self.data[key_columns].describe()
        missing = self.data.isna().sum()
        negative_ghi = (self.data["GHI"] < 0).sum()
        
        return {
            "statistics": stats.to_dict(),
            "missing_values": missing.to_dict(),
            "negative_ghi_count": negative_ghi,
            "timestamp_dtype": str(self.data["Timestamp"].dtype)
        }

    def clean_data(self) -> None:
        """
        Clean data by removing negative GHI/DNI/DHI and imputing missing values with median.
        """
        if self.data is None:
            return
        
        # Remove negative values
        for col in ["GHI", "DNI", "DHI"]:
            self.data = self.data[self.data[col] >= 0]
        
        # Impute missing values with median for numeric columns
        numeric_cols = self.data.select_dtypes(include="number").columns
        for col in numeric_cols:
            self.data[col].fillna(self.data[col].median(), inplace=True)
        
        # Drop rows with missing Timestamp
        self.data.dropna(subset=["Timestamp"], inplace=True)

    def plot_time_series(self, column: str, save_path: Optional[str] = None) -> None:
        """
        Plot time series for a specified column using utils.plot_time_series.

        Args:
            column (str): Column to plot.
            save_path (Optional[str]): Path to save plot.
        """
        if self.data is not None:
            plot_time_series(self.data, column, save_path)