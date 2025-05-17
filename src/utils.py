from typing import Optional, Union, Dict
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

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

def impute_missing_values(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """
    Impute missing values in specified columns with median.

    Args:
        df (pd.DataFrame): Input DataFrame.
        columns (list[str]): Columns to impute.

    Returns:
        pd.DataFrame: DataFrame with imputed values.
    """
    df_copy = df.copy()
    for col in columns:
        if col in df_copy.columns:
            df_copy[col].fillna(df_copy[col].median(), inplace=True)
    return df_copy

def generate_boxplot(data: Dict[str, pd.DataFrame], column: str, save_path: Optional[str] = None) -> None:
    """
    Generate boxplot for a column across multiple datasets.

    Args:
        data (Dict[str, pd.DataFrame]): Dictionary of country names and DataFrames.
        column (str): Column to plot.
        save_path (Optional[str]): Path to save plot.
    """
    combined = pd.DataFrame()
    for country, df in data.items():
        temp = df[[column]].copy()
        temp["Country"] = country
        combined = pd.concat([combined, temp], axis=0)
    
    fig = px.box(combined, x="Country", y=column, title=f"{column} Distribution by Country")
    if save_path:
        fig.write_image(save_path)
    else:
        fig.show()