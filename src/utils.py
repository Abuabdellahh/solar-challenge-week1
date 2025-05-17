def load_data(file_path):
    """Load CSV file with error handling."""
    try:
        import pandas as pd
        return pd.read_csv(file_path)
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return None