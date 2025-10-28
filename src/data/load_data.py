import os
import pandas as pd

def load_data(data_dir="../data/raw"):
    """
    Load and combine all CSV datasets from the raw directory.
    """
    csv_files = [f for f in os.listdir(data_dir) if f.endswith(".csv")]
    dataframes = []

    for file in csv_files:
        path = os.path.join(data_dir, file)
        df = pd.read_csv(path)
        df["source_file"] = file
        dataframes.append(df)
        print(f"✅ Loaded: {file} ({df.shape[0]} rows)")

    combined_df = pd.concat(dataframes, ignore_index=True)
    print(f"\n📊 Combined dataset shape: {combined_df.shape}")
    return combined_df
