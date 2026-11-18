import numpy as np
import pandas as pd
from pathlib import Path

folder = Path(__file__).parent
df = pd.read_csv(folder / "sensor.csv")

# 1. Baris dengan suhu > 30
print("Suhu di atas 30:")
print(df[df["suhu"] > 30])

# 2. Kolom baru
df["suhu_f"] = (df["suhu"] * 9 / 5 + 32).round(1)
df["status"] = np.where(df["suhu"] >= 30, "PANAS", "NORMAL")

# 3. Hitung tiap status
print("\nJumlah per status:")
print(df["status"].value_counts())

# 4. Baris yang suhunya kosong
print("\nBaris dengan suhu kosong:")
print(df[df["suhu"].isna()][["waktu", "sensor", "suhu", "suhu_f", "status"]])

# 5. Tiga suhu tertinggi
print("\nTiga suhu tertinggi:")
print(df.sort_values("suhu", ascending=False).head(3)[["waktu", "sensor", "suhu"]])