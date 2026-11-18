import pandas as pd
from pathlib import Path

folder = Path(__file__).parent
df = pd.read_csv(folder / "sensor.csv")

print("Bentuk:", df.shape)
print("Kolom:", list(df.columns))
print(df.head(3))
print("Data kosong per kolom:")
print(df.isna().sum())
print("Rata-rata suhu:", round(df["suhu"].mean(), 2))
print("Suhu maksimum:", df["suhu"].max())