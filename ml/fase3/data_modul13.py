import numpy as np
import pandas as pd


def buat_data_cpu(n=150, seed=7):
    """Data sintetis Raspberry Pi: suhu CPU dari beban CPU dan suhu ruangan."""
    rng = np.random.default_rng(seed)
    beban = rng.uniform(5, 100, n)               # beban CPU (%)
    suhu_ruang = rng.normal(27, 3, n)            # suhu ruangan (C)
    suhu_cpu = 38 + 0.28 * beban + 0.9 * (suhu_ruang - 27) + rng.normal(0, 1.5, n)
    return pd.DataFrame({
        "beban_cpu": beban.round(1),
        "suhu_ruang": suhu_ruang.round(1),
        "suhu_cpu": suhu_cpu.round(1),
    })