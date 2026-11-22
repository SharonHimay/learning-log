import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import keras
import matplotlib.pyplot as plt
import numpy as np
from keras import layers
from sklearn.datasets import load_digits
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

digits = load_digits()
X = (digits.images / 16.0).astype("float32")[..., None]
y = digits.target
X_latih, X_uji, y_latih, y_uji = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

keras.utils.set_random_seed(0)
model = keras.Sequential([
    keras.Input(shape=(8, 8, 1)),
    layers.Conv2D(8, 3, padding="same", activation="relu"),
    layers.MaxPooling2D(2),
    layers.Conv2D(16, 3, padding="same", activation="relu"),
    layers.MaxPooling2D(2),
    layers.Flatten(),
    layers.Dense(10, activation="softmax"),
])
model.compile(optimizer=keras.optimizers.Adam(learning_rate=0.003),
              loss="sparse_categorical_crossentropy", metrics=["accuracy"])
model.fit(X_latih, y_latih, epochs=30, batch_size=32, validation_split=0.15, verbose=0)

p = model.predict(X_uji, verbose=0)
pred = np.argmax(p, axis=1)
print("Akurasi uji:", round(float(np.mean(pred == y_uji)), 3))
print("Bentuk keluaran predict:", p.shape, " jumlah tiap baris:", round(float(p[0].sum()), 3))

cm = confusion_matrix(y_uji, pred)
print("\nConfusion matrix (baris = sebenarnya, kolom = prediksi):")
print(cm)

print("\nPasangan paling sering tertukar (sebenarnya -> prediksi):")
salah = [(cm[i, j], i, j) for i in range(10) for j in range(10) if i != j and cm[i, j] > 0]
for jumlah, i, j in sorted(salah, reverse=True)[:5]:
    print(f"  {i} -> {j}: {jumlah} kali")

print("\n" + classification_report(y_uji, pred, digits=3))

indeks_salah = np.where(pred != y_uji)[0]
print("Jumlah salah:", len(indeks_salah), " indeks:", indeks_salah.tolist())
yakin = p[indeks_salah].max(axis=1)
print("Keyakinan model pada kesalahan: rata-rata", round(float(yakin.mean()), 3), " minimum", round(float(yakin.min()), 3))
print("Keyakinan model pada tebakan benar: rata-rata", round(float(p[pred == y_uji].max(axis=1).mean()), 3))

fig, sumbu = plt.subplots(2, 5, figsize=(10, 4.5))
for ax, i in zip(sumbu.ravel(), indeks_salah[:10]):
    ax.imshow(X_uji[i, :, :, 0], cmap="gray_r")
    ax.set_title(f"asli {y_uji[i]} / tebak {pred[i]}")
    ax.axis("off")
plt.tight_layout()
plt.savefig("kesalahan.png", dpi=120)
plt.show()