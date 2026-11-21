import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import keras
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

keras.utils.set_random_seed(42)
model = keras.Sequential([
    keras.Input(shape=(2,)),
    layers.Dense(4, activation="relu"),
    layers.Dense(1, activation="sigmoid"),
])
model.compile(optimizer=keras.optimizers.Adam(learning_rate=0.01),
              loss="binary_crossentropy", metrics=["accuracy"])
model.fit(X_latih_s, y_latih, epochs=200, batch_size=32, validation_split=0.2, verbose=0)
print("Akurasi uji:", round(model.evaluate(X_uji_s, y_uji, verbose=0)[1], 3))

# Simpan dan muat ulang
model.save("model_zona.keras")
model_baru = keras.models.load_model("model_zona.keras")
sama = np.allclose(model.predict(X_uji_s, verbose=0), model_baru.predict(X_uji_s, verbose=0))
print("Prediksi model asli dan hasil muat identik:", sama)

# Parameter
W1, b1, W2, b2 = model.get_weights()
print("\nBentuk:", W1.shape, b1.shape, W2.shape, b2.shape)
print("RATA   =", np.round(skala.mean_, 4))
print("SIMPANG=", np.round(skala.scale_, 4))
print("W1 =\n", np.round(W1, 4))
print("b1 =", np.round(b1, 4))
print("W2 =", np.round(W2.ravel(), 4))
print("b2 =", np.round(b2, 4))

contoh = np.array([[15, 50], [27, 50], [38, 50], [21, 60], [33.5, 40], [19.5, 80]])
p = model.predict(skala.transform(contoh), verbose=0).ravel()
print("\nPrediksi Keras:")
for c, pp in zip(contoh, p):
    print(c.tolist(), "P(ALARM)=", round(float(pp), 3))