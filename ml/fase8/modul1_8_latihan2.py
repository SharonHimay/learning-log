import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import keras
import numpy as np
from keras import layers
from sklearn.datasets import load_digits
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

digits = load_digits()
X = (digits.images / 16.0).astype("float32")[..., None]
y = digits.target
X_latih, X_uji, y_latih, y_uji = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

# 1. Bentuk dan baseline
print("Latih:", X_latih.shape, " Uji:", X_uji.shape)
print("Jumlah per kelas (latih):", np.bincount(y_latih).tolist())
rata = lambda a: a.reshape(len(a), -1)
baseline = DummyClassifier(strategy="most_frequent").fit(rata(X_latih), y_latih)
print("Baseline uji:", round(baseline.score(rata(X_uji), y_uji), 3))

# 2. Regresi logistik pada piksel
log = LogisticRegression(max_iter=2000).fit(rata(X_latih), y_latih)
print("Logistik piksel: uji", round(log.score(rata(X_uji), y_uji), 3),
      " parameter", log.coef_.size + log.intercept_.size)


def bangun_mlp():
    return keras.Sequential([
        keras.Input(shape=(8, 8, 1)),
        layers.Flatten(),
        layers.Dense(32, activation="relu"),
        layers.Dense(10, activation="softmax"),
    ])


def bangun_cnn():
    return keras.Sequential([
        keras.Input(shape=(8, 8, 1)),
        layers.Conv2D(8, 3, padding="same", activation="relu"),
        layers.MaxPooling2D(2),
        layers.Conv2D(16, 3, padding="same", activation="relu"),
        layers.MaxPooling2D(2),
        layers.Flatten(),
        layers.Dense(10, activation="softmax"),
    ])


bangun_cnn().summary()

for nama, bangun in [("MLP", bangun_mlp), ("CNN", bangun_cnn)]:
    print(f"\n=== {nama}: parameter {bangun().count_params()} ===")
    akurasi = []
    for seed in range(3):
        keras.utils.set_random_seed(seed)
        model = bangun()
        model.compile(optimizer=keras.optimizers.Adam(learning_rate=0.003),
                      loss="sparse_categorical_crossentropy", metrics=["accuracy"])
        r = model.fit(X_latih, y_latih, epochs=30, batch_size=32,
                      validation_split=0.15, verbose=0)
        akurasi.append(model.evaluate(X_uji, y_uji, verbose=0)[1])
        if seed == 0:
            for e in (1, 10, 30):
                print(f"  seed 0, epoch {e:>2}: loss={r.history['loss'][e-1]:.3f}  "
                      f"val_acc={r.history['val_accuracy'][e-1]:.3f}")
    print("  akurasi uji per seed:", np.round(akurasi, 3).tolist(),
          " rata-rata:", round(float(np.mean(akurasi)), 3))

# 4. MAC per gambar
mac_cnn = 8 * 8 * (3 * 3 * 1) * 8 + 4 * 4 * (3 * 3 * 8) * 16 + 64 * 10
mac_mlp = 64 * 32 + 32 * 10
print("\nMAC per gambar: MLP =", mac_mlp, " CNN =", mac_cnn, " rasio =", round(mac_cnn / mac_mlp, 1))
print("Ukuran float32: MLP =", 2410 * 4, "byte, CNN =", 1898 * 4, "byte")