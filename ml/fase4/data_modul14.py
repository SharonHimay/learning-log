import numpy as np
import pandas as pd


def buat_data_mesin(n=1000, seed=3):
    """Data sintetis motor: ~6% kasus RUSAK, dengan fitur yang tumpang tindih."""
    rng = np.random.default_rng(seed)
    rusak = rng.random(n) < 0.06
    getaran = np.where(rusak, rng.normal(3.0, 0.8, n), rng.normal(2.0, 0.5, n))
    suhu_motor = np.where(rusak, rng.normal(67, 6, n), rng.normal(60, 5, n))
    return pd.DataFrame({
        "getaran": getaran.round(2),
        "suhu_motor": suhu_motor.round(1),
        "kondisi": np.where(rusak, "RUSAK", "NORMAL"),
    })