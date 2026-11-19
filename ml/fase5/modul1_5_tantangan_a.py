import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from data_modul15 import buat_data_motor

df = buat_data_motor()
num = ["getaran", "arus_ma", "suhu_motor"]
X = df[num]
y = df["kondisi"]
X_latih, X_uji, y_latih, y_uji = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y)


def jitter(X, y, sigma_rel, salinan, rng):
    """Tambah salinan data latih dengan noise Gaussian sebesar sigma_rel x std tiap kolom."""
    std = X.std()
    daftar_x, daftar_y = [X], [y]
    for _ in range(salinan):
        noise = rng.normal(0, 1, X.shape) * (std.to_numpy() * sigma_rel)
        daftar_x.append(X + noise)
        daftar_y.append(y)
    return pd.concat(daftar_x, ignore_index=True), pd.concat(daftar_y, ignore_index=True)


hasil = {"tanpa": [], "0.05": [], "0.1": [], "0.3": [], "0.6": []}
for ulang in range(30):
    idx = np.random.default_rng(ulang).choice(len(X_latih), 60, replace=False)
    Xs, ys = X_latih.iloc[idx], y_latih.iloc[idx]
    buat = lambda: make_pipeline(SimpleImputer(strategy="median"), StandardScaler(), LogisticRegression())

    hasil["tanpa"].append(buat().fit(Xs, ys).score(X_uji, y_uji))
    for s in ("0.05", "0.1", "0.3", "0.6"):
        Xa, ya = jitter(Xs, ys, float(s), 4, np.random.default_rng(ulang + 100))
        hasil[s].append(buat().fit(Xa, ya).score(X_uji, y_uji))

for k, v in hasil.items():
    print(f"noise={k:<6} rata-rata={np.mean(v):.3f}  std={np.std(v):.3f}")