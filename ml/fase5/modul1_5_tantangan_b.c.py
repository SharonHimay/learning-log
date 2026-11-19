import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from data_modul15 import buat_data_motor

df = buat_data_motor().dropna()
num = ["getaran", "arus_ma", "suhu_motor"]
X = df[num]
y = df["kondisi"]
X_latih, X_uji, y_latih, y_uji = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y)
print("data lengkap:", df.shape, "latih", X_latih.shape, "uji", X_uji.shape)

model = make_pipeline(StandardScaler(), LogisticRegression())
model.fit(X_latih, y_latih)
print("akurasi uji:", round(model.score(X_uji, y_uji), 3))

skala = model.named_steps["standardscaler"]
logistik = model.named_steps["logisticregression"]
print("kelas:", logistik.classes_)
print("mean_ :", skala.mean_.round(4).tolist())
print("scale_:", skala.scale_.round(4).tolist())
print("coef_ :", logistik.coef_[0].round(4).tolist())
print("intercept_:", logistik.intercept_.round(4).tolist())

kolom = list(logistik.classes_).index("RUSAK")
contoh = pd.DataFrame([[1.5, 900, 55], [2.0, 1000, 60], [2.6, 1100, 66], [3.0, 1200, 70]], columns=num)
for baris, p in zip(contoh.values, model.predict_proba(contoh)[:, kolom]):
    print(baris.tolist(), "P(RUSAK)=", round(float(p), 3))