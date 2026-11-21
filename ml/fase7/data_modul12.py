import numpy as np
import pandas as pd


def buat_data(n=200, seed=42):
    """Data sensor sintetis: status PANAS ditentukan suhu, kelembapan, dan noise."""
    rng = np.random.default_rng(seed)
    suhu = rng.normal(29, 4, n)
    kelembapan = rng.normal(60, 10, n)
    skor = suhu - 0.1 * (kelembapan - 60) + rng.normal(0, 2, n)
    status = np.where(skor >= 30, "PANAS", "NORMAL")
    return pd.DataFrame({
        "suhu": suhu.round(1),
        "kelembapan": kelembapan.round(1),
        "status": status,
    })


if __name__ == "__main__":
    df = buat_data()
    print(df.shape)
    print(df.head())
    print(df["status"].value_counts())
