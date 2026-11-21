import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import keras
import matplotlib.pyplot as plt
import numpy as np
from keras import layers
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from zona import buat_data_zona

df = buat_data_zona()
X = df[["suhu", "kelembapan"]].to_numpy()
y = df["alarm"].to_numpy()
X_latih, X_uji, y_latih, y_uji = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y)
skala = StandardScaler().fit(X_latih)
X_latih_s = skala.transform(X_latih)
X_uji_s = skala.transform(X_uji)


def bangun_model(hidden=4):
    return keras.Sequential([
        keras.Input(shape=(2,)),
        layers.Dense(hidden, activation="relu"),
        layers.Dense(1, activation="sigmoid"),
    ])


def latih(lr, epochs, seed=42):
    keras.utils.set_random_seed(seed)
    model = bangun_model()
    model.compile(optimizer=keras.optimizers.Adam(learning_rate=lr),
                  loss="binary_crossentropy", metrics=["accuracy"])
    riwayat = model.fit(X_latih_s, y_latih, epochs=epochs, batch_size=32,
                        validation_split=0.2, verbose=0)
    return model, riwayat


# 1. Ringkasan model
bangun_model().summary()

# 2. Learning rate bawaan Adam (0.001)
model, riwayat = latih(lr=0.001, epochs=300)
loss, akurasi = model.evaluate(X_uji_s, y_uji, verbose=0)
print("\n=== Adam lr=0.001, 300 epoch ===")
for e in (1, 50, 100, 200, 300):
    print(f"epoch {e:>3}  loss={riwayat.history['loss'][e-1]:.4f}  val_loss={riwayat.history['val_loss'][e-1]:.4f}")
print(f"uji: loss={loss:.4f}  akurasi={akurasi:.3f}")

# 3. Learning rate 0.01
model, riwayat = latih(lr=0.01, epochs=200)
loss, akurasi = model.evaluate(X_uji_s, y_uji, verbose=0)
print("\n=== Adam lr=0.01, 200 epoch ===")
for e in (1, 10, 25, 50, 100, 200):
    print(f"epoch {e:>3}  loss={riwayat.history['loss'][e-1]:.4f}  acc={riwayat.history['accuracy'][e-1]:.3f}  "
          f"val_loss={riwayat.history['val_loss'][e-1]:.4f}  val_acc={riwayat.history['val_accuracy'][e-1]:.3f}")
print(f"uji: loss={loss:.4f}  akurasi={akurasi:.3f}")

p = model.predict(X_uji_s, verbose=0)
print("\nBentuk predict:", p.shape)
print("5 prediksi pertama:", p[:5].ravel().round(3), " label:", y_uji[:5])

# 4. Grafik kurva belajar
plt.plot(riwayat.history["loss"], label="loss latih")
plt.plot(riwayat.history["val_loss"], label="loss validasi")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Kurva belajar jaringan 2-4-1")
plt.legend()
plt.grid(True)
plt.savefig("kurva_belajar.png", dpi=120)
plt.show()