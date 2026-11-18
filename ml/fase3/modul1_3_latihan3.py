import numpy as np
import pandas as pd
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.tree import DecisionTreeClassifier

from data_modul12 import buat_data

df = buat_data()
X = df[["suhu", "kelembapan"]]
y = df["status"]
X_latih, X_uji, y_latih, y_uji = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

# 1. Latih
model = LogisticRegression()
model.fit(X_latih, y_latih)
print("Kelas      :", model.classes_)
print("Koefisien  :", model.coef_[0].round(4))
print("Intercept  :", model.intercept_.round(4))
print("Akurasi latih:", round(model.score(X_latih, y_latih), 3))
print("Akurasi uji  :", round(model.score(X_uji, y_uji), 3))

# 2. Pembanding
baseline = DummyClassifier(strategy="most_frequent").fit(X_latih, y_latih)
pohon = DecisionTreeClassifier(max_depth=2, random_state=42).fit(X_latih, y_latih)
print("\nBaseline uji:", round(baseline.score(X_uji, y_uji), 3))
print("Pohon depth=2 uji:", round(pohon.score(X_uji, y_uji), 3))

# 3. predict_proba
baru = pd.DataFrame(
    [[25, 60], [29, 60], [30, 60], [32, 60], [35, 60], [30, 80]],
    columns=X.columns)
proba = model.predict_proba(baru)
label = model.predict(baru)
print("\nUrutan kolom proba:", model.classes_)
for (suhu, lembap), p, lab in zip(baru.values, proba, label):
    print(f"suhu={suhu:.0f} kelembapan={lembap:.0f}  "
          f"P(NORMAL)={p[0]:.3f}  P(PANAS)={p[1]:.3f}  -> {lab}")

# 4. Ambang
kolom_panas = list(model.classes_).index("PANAS")
p_panas = model.predict_proba(X_uji)[:, kolom_panas]
print("\nPANAS sebenarnya di data uji:", int((y_uji == "PANAS").sum()))
for ambang in (0.5, 0.3, 0.7):
    prediksi = np.where(p_panas >= ambang, "PANAS", "NORMAL")
    jumlah = int((prediksi == "PANAS").sum())
    akurasi = np.mean(prediksi == y_uji)
    print(f"ambang {ambang}: diprediksi PANAS={jumlah}  akurasi={akurasi:.3f}")

# 5. Suhu batas
w = model.coef_[0]
b = model.intercept_[0]
suhu_batas = -(b + w[1] * 60) / w[0]
print("\nSuhu batas pada kelembapan 60:", round(suhu_batas, 2))

# 6. Cross-validation
cv_log = cross_val_score(LogisticRegression(), X, y, cv=5)
cv_pohon = cross_val_score(DecisionTreeClassifier(max_depth=2, random_state=42), X, y, cv=5)
print("\nCV logistik:", cv_log.round(3), "rata-rata", round(cv_log.mean(), 3))
print("CV pohon   :", cv_pohon.round(3), "rata-rata", round(cv_pohon.mean(), 3))