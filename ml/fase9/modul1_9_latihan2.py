import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import GroupKFold, train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

from data_imu import FS, KELAS, buat_data_imu, buat_jendela
from fitur import ekstrak_fitur

# 1. Data dan windowing
data = buat_data_imu()
print("Jumlah rekaman:", len(data), " bentuk satu rekaman:", data[0][2].shape,
      " durasi:", len(data[0][2]) / FS, "detik")
X, y, g = buat_jendela(data, panjang=100, langkah=50)
print("Jendela:", X.shape, " per rekaman:", (len(data[0][2]) - 100) // 50 + 1,
      " per kelas:", np.bincount(y).tolist())
print("Tanpa overlap:", buat_jendela(data, 100, 100)[0].shape,
      " overlap 75%:", buat_jendela(data, 100, 25)[0].shape)

# 2. Fitur
F = ekstrak_fitur(X)
print("Fitur:", F.shape)


def model_logistik():
    return make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000))


def model_pohon():
    return DecisionTreeClassifier(max_depth=5, random_state=0)


MODEL = [("logistik", model_logistik), ("pohon", model_pohon)]

# 3a. Split acak per jendela (BOCOR)
print()
for nama, buat in MODEL:
    hasil = []
    for rs in range(5):
        F_latih, F_uji, y_latih, y_uji = train_test_split(
            F, y, test_size=0.25, random_state=rs, stratify=y)
        hasil.append(buat().fit(F_latih, y_latih).score(F_uji, y_uji))
    print(f"[split ACAK per jendela] {nama}: {np.round(hasil, 3).tolist()} rata-rata {np.mean(hasil):.3f}")

# 3b. Split menurut rekaman: 2 dari 8 rekaman tiap kelas untuk uji
hasil_rekaman = {nama: [] for nama, _ in MODEL}
for rs in range(5):
    rng = np.random.default_rng(rs)
    uji_id = []
    for k in range(4):
        ids = [r[0] for r in data if r[1] == k]
        uji_id += rng.choice(ids, 2, replace=False).tolist()
    mask_uji = np.isin(g, uji_id)
    for nama, buat in MODEL:
        hasil_rekaman[nama].append(buat().fit(F[~mask_uji], y[~mask_uji]).score(F[mask_uji], y[mask_uji]))
for nama, v in hasil_rekaman.items():
    print(f"[split per REKAMAN]      {nama}: {np.round(v, 3).tolist()} rata-rata {np.mean(v):.3f}")

# 3c. GroupKFold
for nama, buat in MODEL:
    skor = []
    for latih, uji in GroupKFold(n_splits=4).split(F, y, g):
        skor.append(buat().fit(F[latih], y[latih]).score(F[uji], y[uji]))
    print(f"GroupKFold(4) {nama}: {np.round(skor, 3).tolist()} rata-rata {np.mean(skor):.3f}")

# 4. Confusion matrix, regresi logistik, pembagian rekaman rs=0
rng = np.random.default_rng(0)
uji_id = []
for k in range(4):
    uji_id += rng.choice([r[0] for r in data if r[1] == k], 2, replace=False).tolist()
mask = np.isin(g, uji_id)
pred = model_logistik().fit(F[~mask], y[~mask]).predict(F[mask])
print("\nRekaman uji:", sorted(uji_id), " akurasi:", round(accuracy_score(y[mask], pred), 3))
print("Urutan kelas:", KELAS)
print(confusion_matrix(y[mask], pred))