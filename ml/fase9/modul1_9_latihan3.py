import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import keras
import numpy as np
from keras import layers
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GroupKFold
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

from data_imu import FS, buat_data_imu, buat_jendela
from fitur import ekstrak_fitur

data = buat_data_imu()
X, y, g = buat_jendela(data, panjang=100, langkah=50)


def bangun_kecil():
    return keras.Sequential([
        keras.Input(shape=(100, 3)),
        layers.Conv1D(8, 5, padding="same", activation="relu"),
        layers.MaxPooling1D(2),
        layers.Conv1D(16, 5, padding="same", activation="relu"),
        layers.GlobalAveragePooling1D(),
        layers.Dense(4, activation="softmax"),
    ])


def bangun_c():
    return keras.Sequential([
        keras.Input(shape=(100, 3)),
        layers.Conv1D(16, 15, padding="same", activation="relu"),
        layers.MaxPooling1D(4),
        layers.Conv1D(32, 7, padding="same", activation="relu"),
        layers.MaxPooling1D(2),
        layers.Flatten(),
        layers.Dropout(0.3),
        layers.Dense(4, activation="softmax"),
    ])


def evaluasi_cnn(bangun, epochs):
    skor = []
    for lipat, (latih, uji) in enumerate(GroupKFold(n_splits=4).split(X, y, g)):
        rata = X[latih].mean(axis=(0, 1))
        std = X[latih].std(axis=(0, 1))
        X_latih, X_uji = (X[latih] - rata) / std, (X[uji] - rata) / std   # skala dari data latih
        keras.utils.set_random_seed(lipat)
        model = bangun()
        model.compile(optimizer=keras.optimizers.Adam(learning_rate=0.003),
                      loss="sparse_categorical_crossentropy", metrics=["accuracy"])
        model.fit(X_latih, y[latih], epochs=epochs, batch_size=32, verbose=0)
        skor.append(model.evaluate(X_uji, y[uji], verbose=0)[1])
    return skor, model.count_params()


bangun_kecil().summary()
skor, n_param = evaluasi_cnn(bangun_kecil, 40)
print(f"\nCNN 1D kecil ({n_param} parameter): {np.round(skor, 3).tolist()} rata-rata {np.mean(skor):.3f}")
skor, n_param = evaluasi_cnn(bangun_c, 60)
print(f"CNN 1D arsitektur C ({n_param} parameter): {np.round(skor, 3).tolist()} rata-rata {np.mean(skor):.3f}")

# Pengaruh panjang jendela (16 fitur, GroupKFold)
print("\nPanjang | durasi | jendela | logistik | pohon | buffer float32")
for W in (25, 50, 100, 200):
    Xw, yw, gw = buat_jendela(data, W, W // 2)
    F = ekstrak_fitur(Xw)
    hasil = {"logistik": [], "pohon": []}
    for latih, uji in GroupKFold(n_splits=4).split(F, yw, gw):
        hasil["logistik"].append(make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000))
                                 .fit(F[latih], yw[latih]).score(F[uji], yw[uji]))
        hasil["pohon"].append(DecisionTreeClassifier(max_depth=5, random_state=0)
                              .fit(F[latih], yw[latih]).score(F[uji], yw[uji]))
    print(f"{W:>3}     | {W / FS:.1f} s | {len(Xw):>5}   | {np.mean(hasil['logistik']):.3f}    | "
          f"{np.mean(hasil['pohon']):.3f} | {W * 3 * 4} byte")