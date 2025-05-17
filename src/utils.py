from typing import Optional, Union
import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path: str) -> Optional[pd.DataFrame]:
    """
    Load CSV file with error handling.

    Args:
        file_path (str): Path to CSV file.

    Returns:
        Optional[pd.DataFrame]: Loaded DataFrame or None if error occurs.
    """
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return None

def compute_z_scores(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """
    Compute Z-scores for specified columns to detect outliers.

    Args:
        df (pd.DataFrame): Input DataFrame.
        columns (list[str]): Columns to compute Z-scores for.

    Returns:
        pd.DataFrame: DataFrame with Z-scores for specified columns.
    """
    z_scores = df[columns].copy()
    for col in columns:
        z_scores[f"{col}_z"] = (df[col] - df[col].mean()) / df[col].std()
    return z_scores

def plot_time_series(df: pd.DataFrame, column: str, save_path: Optional[str] = None) -> None:
    """
    Plot time series for a specified column.

    Args:
        df (pd.DataFrame): DataFrame with 'Timestamp' and target column.
        column (str): Column to plot.
        save_path (Optional[str]): Path to save plot (default: None, displays plot).
    """
    plt.figure(figsize=(10, 6))
    plt.plot(df["Timestamp"], df[column], label=column)
    plt.xlabel("Timestamp")
    plt.ylabel(column)
    plt.title(f"{column} Time Series")
    plt.legend()
    plt.grid(True)
    if save_path:
        plt.savefig(save_path)
        plt.close()
    else:
        plt.show()