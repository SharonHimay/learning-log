import pandas as pd
from pathlib import Path

folder = Path(__file__).parent
df = pd.read_csv(folder / "sensor.csv")

# 1. Rata-rata suhu per sensor
print("Rata-rata suhu per sensor:")
print(df.groupby("sensor")["suhu"].mean().round(2))

# 2. Isi data hilang dengan rata-rata per sensor
df["suhu"] = df["suhu"].fillna(df.groupby("sensor")["suhu"].transform("mean"))
df["kelembapan"] = df["kelembapan"].fillna(df.groupby("sensor")["kelembapan"].transform("mean"))

# 3. Cek tidak ada yang kosong, lihat baris 5 dan 8
print("\nTotal data kosong:", df.isna().sum().sum())
print(df.loc[[5, 8]])

# 4. Simpan dan baca ulang
df.to_csv("bersih.csv", index=False)
cek = pd.read_csv("bersih.csv")
print("\nBentuk bersih.csv:", cek.shape)

# 5. Rata-rata per sensor setelah pembersihan
print("\nRata-rata setelah pembersihan:")
print(df.groupby("sensor")[["suhu", "kelembapan"]].mean().round(2))