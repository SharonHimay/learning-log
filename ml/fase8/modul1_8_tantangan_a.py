import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import keras
import numpy as np
from keras import layers
from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

digits = load_digits()
X = (digits.images / 16.0).astype("float32")[..., None]
y = digits.target
X_latih, X_uji, y_latih, y_uji = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)


def geser(gambar, dy, dx):
    """Geser gambar (n,8,8,1) sejauh dy baris dan dx kolom; sisanya diisi 0."""
    keluar = np.zeros_like(gambar)
    h, w = gambar.shape[1], gambar.shape[2]
    ys, yd = (slice(0, h - dy), slice(dy, h)) if dy >= 0 else (slice(-dy, h), slice(0, h + dy))
    xs, xd = (slice(0, w - dx), slice(dx, w)) if dx >= 0 else (slice(-dx, w), slice(0, w + dx))
    keluar[:, yd, xd, :] = gambar[:, ys, xs, :]
    return keluar


def augmentasi_geser(gambar, label, rng, salinan=3):
    daftar, lab = [gambar], [label]
    for _ in range(salinan):
        baru = np.empty_like(gambar)
        for i in range(len(gambar)):
            dy, dx = rng.integers(-1, 2, size=2)       # geser -1, 0, atau +1 piksel
            baru[i] = geser(gambar[i:i + 1], int(dy), int(dx))[0]
        daftar.append(baru)
        lab.append(label)
    return np.concatenate(daftar), np.concatenate(lab)


ARAH = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def akurasi_geser(prediksi):
    return float(np.mean([np.mean(prediksi(geser(X_uji, dy, dx)) == y_uji) for dy, dx in ARAH]))


def bangun_mlp():
    return keras.Sequential([keras.Input(shape=(8, 8, 1)), layers.Flatten(),
                             layers.Dense(32, activation="relu"), layers.Dense(10, activation="softmax")])


def bangun_cnn():
    return keras.Sequential([
        keras.Input(shape=(8, 8, 1)),
        layers.Conv2D(8, 3, padding="same", activation="relu"), layers.MaxPooling2D(2),
        layers.Conv2D(16, 3, padding="same", activation="relu"), layers.MaxPooling2D(2),
        layers.Flatten(), layers.Dense(10, activation="softmax")])


# Regresi logistik
log = LogisticRegression(max_iter=2000).fit(X_latih.reshape(len(X_latih), -1), y_latih)
pl = lambda g: log.predict(g.reshape(len(g), -1))
print("Logistik: normal", round(float(np.mean(pl(X_uji) == y_uji)), 3),
      " digeser 1 piksel (rata-rata 4 arah)", round(akurasi_geser(pl), 3))

# Tanpa augmentasi, dan dengan augmentasi
for nama, bangun, augmentasi, epoch in [
        ("MLP", bangun_mlp, False, 30), ("CNN", bangun_cnn, False, 30),
        ("MLP+aug", bangun_mlp, True, 15), ("CNN+aug", bangun_cnn, True, 15)]:
    normal, digeser = [], []
    for seed in range(3):
        Xt, yt = X_latih, y_latih
        if augmentasi:
            Xt, yt = augmentasi_geser(X_latih, y_latih, np.random.default_rng(seed))
        keras.utils.set_random_seed(seed)
        model = bangun()
        model.compile(optimizer=keras.optimizers.Adam(learning_rate=0.003),
                      loss="sparse_categorical_crossentropy", metrics=["accuracy"])
        model.fit(Xt, yt, epochs=epoch, batch_size=32, verbose=0)
        prediksi = lambda g: np.argmax(model.predict(g, verbose=0), axis=1)
        normal.append(float(np.mean(prediksi(X_uji) == y_uji)))
        digeser.append(akurasi_geser(prediksi))
    print(f"{nama}: normal {np.round(normal, 3).tolist()} rata-rata {np.mean(normal):.3f} | "
          f"digeser {np.round(digeser, 3).tolist()} rata-rata {np.mean(digeser):.3f}  (ukuran latih {len(Xt)})")