import pandas as pd
from pathlib import Path

raw_path = Path("data/raw/stores_sales_forecasting.csv")
processed_path = Path("data/processed/cleaned_sales.parquet")

def clean_data():
    df = pd.read_csv(raw_path,encoding='ISO-8859-1', parse_dates = True)

    # Column Name cleanup
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

    df = df.dropna(subset=["sales", "order_date"])

    processed_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(processed_path, index=False)

    print(f"Cleaned data saved to {processed_path}")

if __name__ == "__main__":
    clean_data()