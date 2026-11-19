import numpy as np
import pandas as pd


def buat_data_motor(n=400, seed=5):
    """Data sintetis motor dengan skala fitur berbeda, kolom kategori, dan data hilang."""
    rng = np.random.default_rng(seed)
    lokasi = rng.choice(["lab", "gudang", "luar"], n, p=[0.4, 0.4, 0.2])
    beban = rng.choice(["rendah", "sedang", "tinggi"], n, p=[0.3, 0.5, 0.2])
    getaran = rng.normal(2.0, 0.5, n)             # satuan g
    arus = rng.normal(1000, 150, n)               # satuan mA
    suhu = rng.normal(60, 5, n)                   # satuan C

    pengaruh_beban = pd.Series(beban).map({"rendah": 0.0, "sedang": 0.4, "tinggi": 0.9}).to_numpy()
    pengaruh_lokasi = np.where(lokasi == "luar", 0.6, 0.0)
    z = (1.5 * (getaran - 2.0) / 0.5
         + 0.5 * (suhu - 60) / 5
         + 0.2 * (arus - 1000) / 150
         + pengaruh_beban + pengaruh_lokasi
         + rng.normal(0, 0.8, n))
    kondisi = np.where(z > 1.5, "RUSAK", "NORMAL")

    df = pd.DataFrame({
        "getaran": getaran.round(2),
        "arus_ma": arus.round(0),
        "suhu_motor": suhu.round(1),
        "lokasi": lokasi,
        "beban": beban,
        "kondisi": kondisi,
    })
    # Sebagian pembacaan hilang
    df.loc[rng.random(n) < 0.05, "suhu_motor"] = np.nan
    df.loc[rng.random(n) < 0.04, "arus_ma"] = np.nan
    return df