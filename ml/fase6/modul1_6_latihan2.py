import sys
from pathlib import Path

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

sys.path.append(str(Path(__file__).parent.parent / "fase2"))
from data_modul12 import buat_data
from nn import bce, latih_neuron, sigmoid

df = buat_data()
X = df[["suhu", "kelembapan"]].to_numpy()
y = (df["status"] == "PANAS").astype(int).to_numpy()

X_latih, X_uji, y_latih, y_uji = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

skala = StandardScaler().fit(X_latih)
X_latih_s = skala.transform(X_latih)
X_uji_s = skala.transform(X_uji)
print("mean_ :", skala.mean_.round(3), " scale_:", skala.scale_.round(3))

# 1. Latih neuron
w, b, riwayat = latih_neuron(X_latih_s, y_latih, lr=0.1, epoch=500)
for e in (1, 2, 10, 50, 100, 200, 500):
    print(f"epoch {e:>3}  loss {riwayat[e - 1]:.4f}")

p_latih = sigmoid(X_latih_s @ w + b)
p_uji = sigmoid(X_uji_s @ w + b)
print("\nw:", w.round(4), " b:", round(b, 4))
print("Akurasi latih:", round(np.mean((p_latih >= 0.5) == y_latih), 3),
      " uji:", round(np.mean((p_uji >= 0.5) == y_uji), 3))
print("Loss uji:", round(bce(p_uji, y_uji), 4))

# 2. Pembanding scikit-learn
hampir_tanpa = LogisticRegression(C=1e6, max_iter=1000).fit(X_latih_s, y_latih)
bawaan = LogisticRegression().fit(X_latih_s, y_latih)
print("\nsklearn C=1e6 :", hampir_tanpa.coef_[0].round(4), hampir_tanpa.intercept_.round(4),
      "uji", round(hampir_tanpa.score(X_uji_s, y_uji), 3))
print("sklearn bawaan:", bawaan.coef_[0].round(4), bawaan.intercept_.round(4),
      "uji", round(bawaan.score(X_uji_s, y_uji), 3))

# 3. Laju belajar
print("\n=== Laju belajar ===")
for lr in (0.001, 0.01, 0.1, 1.0, 5.0, 50.0):
    w2, b2, r2 = latih_neuron(X_latih_s, y_latih, lr=lr, epoch=500)
    p2 = sigmoid(X_uji_s @ w2 + b2)
    print(f"lr={lr:<6} loss akhir={r2[-1]:.4f}  loss tertinggi={max(r2):.3f}  "
          f"akurasi uji={np.mean((p2 >= 0.5) == y_uji):.3f}")