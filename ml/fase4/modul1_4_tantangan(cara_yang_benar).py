import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_predict, train_test_split

from data_modul14 import buat_data_mesin

df = buat_data_mesin()
X = df[["getaran", "suhu_motor"]]
y = df["kondisi"]
X_latih, X_uji, y_latih, y_uji = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y)

model = LogisticRegression()
kolom = list(model.fit(X_latih, y_latih).classes_).index("RUSAK")

# Pilih ambang HANYA dari data latih (prediksi hasil cross-validation)
p_cv = cross_val_predict(LogisticRegression(), X_latih, y_latih, cv=5,
                         method="predict_proba")[:, kolom]
nyata_latih = (y_latih == "RUSAK").to_numpy()

terbaik = None
for ambang in np.arange(0.05, 0.96, 0.05):
    pred = p_cv >= ambang
    fn = int((~pred & nyata_latih).sum())
    fp = int((pred & ~nyata_latih).sum())
    biaya = 10 * fn + fp
    if terbaik is None or biaya < terbaik[1]:
        terbaik = (round(float(ambang), 2), biaya, fn, fp)
print("Ambang terbaik dari CV pada data latih:", terbaik)

# Uji SEKALI di data uji
p_uji = model.predict_proba(X_uji)[:, kolom]
nyata_uji = (y_uji == "RUSAK").to_numpy()
pred = p_uji >= terbaik[0]
fn = int((~pred & nyata_uji).sum())
fp = int((pred & ~nyata_uji).sum())
print("Di data uji dengan ambang itu: FN =", fn, " FP =", fp, " biaya =", 10 * fn + fp)
print(confusion_matrix(nyata_uji, pred).tolist())