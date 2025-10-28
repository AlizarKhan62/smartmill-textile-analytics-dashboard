import pandas as pd
import numpy as np

def preprocess_data(df):
    """
    Clean and prepare the textile/machine data for analysis.
    """
    df = df.drop_duplicates()
    df = df.dropna(subset=["Machine_ID", "Date", "Output", "Downtime"], how="any")

    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df["Efficiency"] = np.where(df["Capacity"] > 0, (df["Output"] / df["Capacity"]) * 100, np.nan)
    df["Efficiency"] = df["Efficiency"].clip(0, 100)

    df["Downtime_Hours"] = df["Downtime"].apply(lambda x: float(str(x).split()[0]) if pd.notna(x) else 0)
    df["Shift"] = df["Shift"].fillna("Unknown")

    print("✅ Data preprocessing completed!")
    print("Final shape:", df.shape)
    return df
