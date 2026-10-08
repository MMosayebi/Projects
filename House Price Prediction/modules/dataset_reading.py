from pathlib import Path
import pandas as pd
import openpyxl

def read_dataset():
    base_dir = Path(__file__).resolve().parent.parent
    file_path = base_dir / "dataset" / "HousePrice.csv"

    return pd.read_csv(file_path)