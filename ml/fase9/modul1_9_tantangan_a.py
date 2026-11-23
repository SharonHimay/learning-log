import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

from data_imu import buat_data_imu, buat_jendela
from fitur import ekstrak_fitur

data = buat_data_imu(rekaman_per_kelas=24, seed=11)
rng = np.random.default_rng(0)
# uji: 6 rekaman per kelas (tetap); sisanya (18 per kelas) = kumpulan latih
uji_id, kumpulan = [], {k: [] for k in range(4)}
for k in range(4):
    ids = [r[0] for r in data if r[1] == k]
    acak = rng.permutation(ids).tolist()
    uji_id += acak[:6]
    kumpulan[k] = acak[6:]


def evaluasi(latih_id, langkah=50):
    sel_latih = [r for r in data if r[0] in latih_id]
    sel_uji = [r for r in data if r[0] in uji_id]
    X_latih, y_latih, _ = buat_jendela(sel_latih, 100, langkah)
    X_uji, y_uji, _ = buat_jendela(sel_uji, 100, 50)
    F_latih, F_uji = ekstrak_fitur(X_latih), ekstrak_fitur(X_uji)
    hasil = {}
    hasil["logistik"] = make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000)) \
        .fit(F_latih, y_latih).score(F_uji, y_uji)
    hasil["pohon"] = DecisionTreeClassifier(max_depth=5, random_state=0) \
        .fit(F_latih, y_latih).score(F_uji, y_uji)
    return hasil, len(X_latih)


print("=== Jumlah rekaman latih per kelas (rata-rata 5 pengambilan) ===")
for n in (2, 4, 8, 12, 18):
    h = {"logistik": [], "pohon": []}
    jml = 0
    for ulang in range(5):
        r = np.random.default_rng(100 + ulang)
        latih_id = []
        for k in range(4):
            latih_id += r.choice(kumpulan[k], n, replace=False).tolist()
        hasil, jml = evaluasi(latih_id)
        for kunci in h:
            h[kunci].append(hasil[kunci])
    print(f"n={n:>2}/kelas  (jendela latih {jml:>4})  logistik {np.mean(h['logistik']):.3f}  pohon {np.mean(h['pohon']):.3f}")

print("\n=== Jendela lebih banyak dari rekaman yang SAMA (8 per kelas) ===")
for langkah, nama in [(100, "tanpa overlap"), (50, "overlap 50%"), (25, "overlap 75%"), (10, "overlap 90%")]:
    h = {"logistik": [], "pohon": []}
    jml = 0
    for ulang in range(5):
        r = np.random.default_rng(100 + ulang)
        latih_id = []
        for k in range(4):
            latih_id += r.choice(kumpulan[k], 8, replace=False).tolist()
        hasil, jml = evaluasi(latih_id, langkah)
        for kunci in h:
            h[kunci].append(hasil[kunci])
    print(f"{nama:<14} (jendela latih {jml:>5})  logistik {np.mean(h['logistik']):.3f}  pohon {np.mean(h['pohon']):.3f}")