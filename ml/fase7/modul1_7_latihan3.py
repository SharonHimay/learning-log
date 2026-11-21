import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import keras
import matplotlib.pyplot as plt
import numpy as np
from keras import layers, regularizers
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
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
X_latih_p = prep.fit_transform(X_latih)
X_uji_p = prep.transform(X_uji)

# Data latih sengaja dikecilkan: 120 untuk melatih, 180 sisanya untuk validasi
X_k, y_k = X_latih_p[:120], y_latih[:120]
X_val, y_val = X_latih_p[120:], y_latih[120:]
print("Latih kecil:", X_k.shape, " Validasi:", X_val.shape, " Uji (belum disentuh):", X_uji_p.shape)


def bangun(jenis):
    n = X_k.shape[1]
    if jenis == "kecil":
        lapis = [layers.Dense(4, activation="relu")]
    elif jenis == "besar":
        lapis = [layers.Dense(64, activation="relu"), layers.Dense(64, activation="relu")]
    else:   # besar + Dropout + L2
        lapis = [layers.Dense(64, activation="relu", kernel_regularizer=regularizers.l2(0.01)),
                 layers.Dropout(0.3),
                 layers.Dense(64, activation="relu", kernel_regularizer=regularizers.l2(0.01)),
                 layers.Dropout(0.3)]
    return keras.Sequential([keras.Input(shape=(n,))] + lapis + [layers.Dense(1, activation="sigmoid")])


kurva = {}
for nama, jenis in [("kecil", "kecil"), ("besar", "besar"), ("besar+regularisasi", "reg")]:
    keras.utils.set_random_seed(0)
    model = bangun(jenis)
    model.compile(optimizer=keras.optimizers.Adam(learning_rate=0.003),
                  loss="binary_crossentropy", metrics=["accuracy"])
    r = model.fit(X_k, y_k, epochs=300, batch_size=16,
                  validation_data=(X_val, y_val), verbose=0)
    kurva[nama] = r.history
    best = int(np.argmin(r.history["val_loss"])) + 1
    print(f"\n{nama:<20} parameter={model.count_params():>5}")
    print(f"   epoch val_loss terendah = {best}  (val_loss {min(r.history['val_loss']):.3f})")
    print(f"   di epoch 300: loss latih={r.history['loss'][-1]:.3f}  val_loss={r.history['val_loss'][-1]:.3f}  "
          f"akurasi latih={r.history['accuracy'][-1]:.3f}  akurasi validasi={r.history['val_accuracy'][-1]:.3f}")

for nama, h in kurva.items():
    plt.plot(h["val_loss"], label=f"val_loss {nama}")
plt.xlabel("Epoch")
plt.ylabel("Loss validasi")
plt.ylim(0, 1.5)
plt.title("Overfitting pada data latih kecil")
plt.legend()
plt.grid(True)
plt.savefig("overfitting.png", dpi=120)
plt.show()

# Early stopping pada model besar tanpa regularisasi
keras.utils.set_random_seed(0)
model = bangun("besar")
model.compile(optimizer=keras.optimizers.Adam(learning_rate=0.003),
              loss="binary_crossentropy", metrics=["accuracy"])
berhenti = keras.callbacks.EarlyStopping(monitor="val_loss", patience=15, restore_best_weights=True)
r = model.fit(X_k, y_k, epochs=300, batch_size=16, validation_data=(X_val, y_val),
              callbacks=[berhenti], verbose=0)
print(f"\nModel besar + EarlyStopping(patience=15): berhenti di epoch {len(r.history['loss'])}, "
      f"val_loss terbaik={min(r.history['val_loss']):.3f}")
print("Akurasi uji (dipakai sekali):", round(model.evaluate(X_uji_p, y_uji, verbose=0)[1], 3))