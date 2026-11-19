import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, precision_recall_curve
from sklearn.model_selection import train_test_split

from data_modul14 import buat_data_mesin

df = buat_data_mesin()
X = df[["getaran", "suhu_motor"]]
y = df["kondisi"]
X_latih, X_uji, y_latih, y_uji = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y)

model = LogisticRegression().fit(X_latih, y_latih)
kolom_rusak = list(model.classes_).index("RUSAK")
p = model.predict_proba(X_uji)[:, kolom_rusak]
nyata = (y_uji == "RUSAK").to_numpy()

# 1. Biaya total
print("=== Biaya total (FN=10, FP=1) ===")
terbaik = None
for ambang in np.arange(0.05, 0.96, 0.05):
    pred = p >= ambang
    fn = int((~pred & nyata).sum())
    fp = int((pred & ~nyata).sum())
    biaya = 10 * fn + 1 * fp
    if terbaik is None or biaya < terbaik[1]:
        terbaik = (round(float(ambang), 2), biaya, fn, fp)
    print(f"ambang {ambang:.2f}: FN={fn:>2}  FP={fp:>3}  biaya={biaya}")
print("Terbaik (ambang, biaya, FN, FP):", terbaik)

# 2. Recall minimal 0,8
presisi, recall, ambang_arr = precision_recall_curve(nyata.astype(int), p)
kandidat = [(t, pr, rc) for t, pr, rc in zip(ambang_arr, presisi[:-1], recall[:-1]) if rc >= 0.8]
t, pr, rc = max(kandidat, key=lambda x: x[0])
print(f"\nAmbang tertinggi dengan recall >= 0.8: {t:.3f}")
print(f"precision={pr:.3f}  recall={rc:.3f}")
print(confusion_matrix(nyata, p >= t).tolist())