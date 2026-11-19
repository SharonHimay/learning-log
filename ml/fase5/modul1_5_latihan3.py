import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, precision_score, recall_score
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler

from data_modul15 import buat_data_motor

df = buat_data_motor()
y = df["kondisi"]
X = df.drop(columns="kondisi")
X_latih, X_uji, y_latih, y_uji = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y)
print("Latih:", X_latih.shape, y_latih.value_counts().to_dict())
print("Uji  :", X_uji.shape, y_uji.value_counts().to_dict())
print("Baseline uji:", DummyClassifier(strategy="most_frequent").fit(X_latih, y_latih).score(X_uji, y_uji))

numerik = ["getaran", "arus_ma", "suhu_motor"]
prep_num = Pipeline([
    ("isi", SimpleImputer(strategy="median")),
    ("skala", StandardScaler()),
])
prep = ColumnTransformer([
    ("num", prep_num, numerik),
    ("lokasi", OneHotEncoder(handle_unknown="ignore"), ["lokasi"]),
    ("beban", OrdinalEncoder(categories=[["rendah", "sedang", "tinggi"]]), ["beban"]),
])
model = Pipeline([("prep", prep), ("clf", LogisticRegression())])

# 1. Latih dan evaluasi
model.fit(X_latih, y_latih)
print("\nLengkap -> latih:", round(model.score(X_latih, y_latih), 3),
      " uji:", round(model.score(X_uji, y_uji), 3))
cv = cross_val_score(model, X, y, cv=5)
print("CV:", cv.round(3), "rata-rata", round(cv.mean(), 3))

# 2. Nama fitur dan koefisien
print("\nFitur:", list(model.named_steps["prep"].get_feature_names_out()))
print("Koefisien:", model.named_steps["clf"].coef_[0].round(3))
print("Intercept:", model.named_steps["clf"].intercept_.round(3))

# 3. Confusion matrix
pred = model.predict(X_uji)
print("\nConfusion matrix:", confusion_matrix(y_uji, pred, labels=["NORMAL", "RUSAK"]).tolist())
print("Precision RUSAK:", round(precision_score(y_uji, pred, pos_label="RUSAK"), 3))
print("Recall RUSAK   :", round(recall_score(y_uji, pred, pos_label="RUSAK"), 3))

# 4. Hanya numerik
model_num = Pipeline([
    ("prep", ColumnTransformer([("num", prep_num, numerik)])),
    ("clf", LogisticRegression()),
])
model_num.fit(X_latih, y_latih)
cv_num = cross_val_score(model_num, X, y, cv=5)
print("\nHanya numerik -> uji:", round(model_num.score(X_uji, y_uji), 3),
      " CV:", round(cv_num.mean(), 3))

# 5. Demonstrasi kebocoran
X_num = X[numerik]
median_semua = X_num.median()
median_latih = X_latih[numerik].median()
Xn_semua = X_num.fillna(median_semua)
Xl_n = X_latih[numerik].fillna(median_latih)
Xu_n = X_uji[numerik].fillna(median_latih)

skala_bocor = StandardScaler().fit(Xn_semua)
skala_benar = StandardScaler().fit(Xl_n)
print("\nRata-rata data uji (skala dari SEMUA data):", skala_bocor.transform(Xu_n).mean(axis=0).round(3))
print("Rata-rata data uji (skala dari data LATIH):", skala_benar.transform(Xu_n).mean(axis=0).round(3))
print("Data latih setelah skala -> rata-rata:", skala_benar.transform(Xl_n).mean(axis=0).round(3),
      " std:", skala_benar.transform(Xl_n).std(axis=0).round(3))
print("mean_ :", skala_benar.mean_.round(3), " scale_:", skala_benar.scale_.round(3))