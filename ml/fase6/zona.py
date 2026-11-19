import numpy as np
import pandas as pd


def buat_data_zona(n=300, seed=1):
    """Alarm kalau terlalu dingin ATAU terlalu panas: zona aman hanya di tengah."""
    rng = np.random.default_rng(seed)
    suhu = rng.uniform(10, 45, n)
    kelembapan = rng.uniform(20, 90, n)
    alarm = (suhu < 20) | (suhu > 33)
    return pd.DataFrame({
        "suhu": suhu.round(1),
        "kelembapan": kelembapan.round(1),
        "alarm": alarm.astype(int),
    })