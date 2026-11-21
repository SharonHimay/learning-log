import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import keras
import numpy as np
from keras import layers
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler

from data_modul15 import buat_data_motor

df = buat_data_motor()
y = (df["kondisi"] == "RUSAK").astype(int).to_numpy()
X = df.drop(columns="kondisi")
X_latih, X_uji, y_latih, y_uji = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y)

numerik = ["getaran", "arus_ma", "suhu_motor"]
prep = ColumnTransformer([
    ("num", Pipeline([("isi", SimpleImputer(strategy="median")),
                      ("skala", StandardScaler())]), numerik),
    ("lokasi", OneHotEncoder(handle_unknown="ignore", sparse_output=False), ["lokasi"]),
    ("beban", OrdinalEncoder(categories=[["rendah", "sedang", "tinggi"]]), ["beban"]),
])
X_latih_p = prep.fit_transform(X_latih)      # fit HANYA di data latih
X_uji_p = prep.transform(X_uji)
print("Bentuk setelah preprocessing:", X_latih_p.shape, X_uji_p.shape)


def bangun_model(n_fitur):
    return keras.Sequential([
        keras.Input(shape=(n_fitur,)),
        layers.Dense(16, activation="relu"),
        layers.Dense(8, activation="relu"),
        layers.Dense(1, activation="sigmoid"),
    ])


hasil = []
for seed in range(3):
    keras.utils.set_random_seed(seed)
    model = bangun_model(X_latih_p.shape[1])
    model.compile(optimizer=keras.optimizers.Adam(learning_rate=0.003),
                  loss="binary_crossentropy", metrics=["accuracy"])
    berhenti = keras.callbacks.EarlyStopping(monitor="val_loss", patience=20,
                                             restore_best_weights=True)
    riwayat = model.fit(X_latih_p, y_latih, epochs=300, batch_size=32,
                        validation_split=0.2, callbacks=[berhenti], verbose=0)
    epoch_terbaik = int(np.argmin(riwayat.history["val_loss"])) + 1
    epoch_total = len(riwayat.history["loss"])
    p = model.predict(X_uji_p, verbose=0).ravel()
    pred = (p >= 0.5).astype(int)
    akurasi = float(np.mean(pred == y_uji))
    prec = precision_score(y_uji, pred)
    rec = recall_score(y_uji, pred)
    hasil.append(akurasi)
    print(f"seed={seed}: berhenti di epoch {epoch_total} (terbaik {epoch_terbaik})  "
          f"akurasi uji={akurasi:.3f}  precision={prec:.3f}  recall={rec:.3f}  "
          f"cm={confusion_matrix(y_uji, pred).tolist()}")
print("Rata-rata akurasi uji (3 seed):", round(float(np.mean(hasil)), 3))

# Pembanding: regresi logistik di data yang sama
log = LogisticRegression().fit(X_latih_p, y_latih)
pred_log = log.predict(X_uji_p)
print("\nRegresi logistik: akurasi uji =", round(float(np.mean(pred_log == y_uji)), 3),
      " precision =", round(precision_score(y_uji, pred_log), 3),
      " recall =", round(recall_score(y_uji, pred_log), 3))
print("Baseline (selalu NORMAL):", round(float(np.mean(y_uji == 0)), 3))