import numpy as np
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score, confusion_matrix, f1_score,
                             precision_score, recall_score, roc_auc_score)
from sklearn.model_selection import train_test_split

from data_modul14 import buat_data_mesin

df = buat_data_mesin()
X = df[["getaran", "suhu_motor"]]
y = df["kondisi"]
X_latih, X_uji, y_latih, y_uji = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y)

# 1. Jumlah kelas
print("Semua :", df["kondisi"].value_counts().to_dict())
print("Latih :", y_latih.value_counts().to_dict())
print("Uji   :", y_uji.value_counts().to_dict())


def laporan(nama, pred):
    cm = confusion_matrix(y_uji, pred, labels=["NORMAL", "RUSAK"])
    print(f"{nama:<20} {cm.tolist()}  "
          f"akurasi={accuracy_score(y_uji, pred):.3f}  "
          f"precision={precision_score(y_uji, pred, pos_label='RUSAK', zero_division=0):.3f}  "
          f"recall={recall_score(y_uji, pred, pos_label='RUSAK'):.3f}  "
          f"F1={f1_score(y_uji, pred, pos_label='RUSAK', zero_division=0):.3f}")


# 2. Tiga model
baseline = DummyClassifier(strategy="most_frequent").fit(X_latih, y_latih)
biasa = LogisticRegression().fit(X_latih, y_latih)
seimbang = LogisticRegression(class_weight="balanced").fit(X_latih, y_latih)

print("\n=== Tiga model ===")
laporan("Baseline", baseline.predict(X_uji))
laporan("Logistik biasa", biasa.predict(X_uji))
laporan("Logistik balanced", seimbang.predict(X_uji))

# 3. AUC
kolom_rusak = list(biasa.classes_).index("RUSAK")
p_rusak = biasa.predict_proba(X_uji)[:, kolom_rusak]
print("\nAUC (model biasa):", round(roc_auc_score((y_uji == "RUSAK").astype(int), p_rusak), 3))

# 4. Ambang
print("\n=== Ambang pada model biasa ===")
for ambang in (0.5, 0.3, 0.2, 0.1, 0.05):
    laporan(f"ambang {ambang}", np.where(p_rusak >= ambang, "RUSAK", "NORMAL"))