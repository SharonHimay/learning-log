import numpy as np
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

from nn import latih_jaringan, prediksi_jaringan
from zona import buat_data_zona

df = buat_data_zona()
print("Bentuk:", df.shape, " Alarm:", df["alarm"].value_counts().to_dict())

X = df[["suhu", "kelembapan"]].to_numpy()
y = df["alarm"].to_numpy()
X_latih, X_uji, y_latih, y_uji = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y)

skala = StandardScaler().fit(X_latih)
X_latih_s = skala.transform(X_latih)
X_uji_s = skala.transform(X_uji)
print("Latih/uji:", X_latih.shape, X_uji.shape)

# Pembanding
print("\nBaseline uji:", round(DummyClassifier(strategy="most_frequent").fit(X_latih, y_latih).score(X_uji, y_uji), 3))
print("Logistik uji:", round(LogisticRegression().fit(X_latih_s, y_latih).score(X_uji_s, y_uji), 3))
print("Pohon d=2 uji:", round(DecisionTreeClassifier(max_depth=2, random_state=0).fit(X_latih, y_latih).score(X_uji, y_uji), 3))

# Jaringan 2-4-1 (ReLU), seed 0
parameter, riwayat = latih_jaringan(X_latih_s, y_latih, hidden=4, lr=0.5, epoch=3000, seed=0)
print("\nLoss pada epoch:", {e: round(riwayat[e - 1], 4) for e in (1, 10, 100, 500, 1000, 3000)})
p_latih = prediksi_jaringan(parameter, X_latih_s)
p_uji = prediksi_jaringan(parameter, X_uji_s)
print("Akurasi latih:", round(np.mean((p_latih >= 0.5) == y_latih), 3),
      " uji:", round(np.mean((p_uji >= 0.5) == y_uji), 3))
print("Jumlah parameter:", sum(p.size for p in parameter))

# Pengaruh jumlah neuron tersembunyi, 5 inisialisasi acak berbeda
print("\n=== Hidden units x 5 seed (akurasi uji) ===")
for aktivasi in ("relu", "tanh"):
    for hidden in (1, 2, 4, 8):
        akurasi = []
        for seed in range(5):
            par, _ = latih_jaringan(X_latih_s, y_latih, hidden=hidden, lr=0.5,
                                    epoch=3000, seed=seed, aktivasi=aktivasi)
            p = prediksi_jaringan(par, X_uji_s, aktivasi)
            akurasi.append(np.mean((p >= 0.5) == y_uji))
        print(f"{aktivasi:<5} hidden={hidden}  per seed={np.round(akurasi, 3).tolist()}  rata-rata={np.mean(akurasi):.3f}")