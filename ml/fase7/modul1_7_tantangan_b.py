import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import keras
import numpy as np
from keras import layers
from sklearn.model_selection import train_test_split

from zona import buat_data_zona

df = buat_data_zona()
X = df[["suhu", "kelembapan"]].to_numpy()
y = df["alarm"].to_numpy()
X_latih, X_uji, y_latih, y_uji = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y)

keras.utils.set_random_seed(42)
norm = layers.Normalization()
norm.adapt(X_latih)                     # belajar rata-rata dan varians dari data latih mentah

model = keras.Sequential([
    keras.Input(shape=(2,)),
    norm,
    layers.Dense(4, activation="relu"),
    layers.Dense(1, activation="sigmoid"),
])
model.compile(optimizer=keras.optimizers.Adam(learning_rate=0.01),
              loss="binary_crossentropy", metrics=["accuracy"])
model.fit(X_latih, y_latih, epochs=200, batch_size=32, validation_split=0.2, verbose=0)

print("Akurasi uji (data mentah):", round(model.evaluate(X_uji, y_uji, verbose=0)[1], 3))
dilatih = int(sum(np.prod(w.shape) for w in model.trainable_weights))
print("Parameter total:", model.count_params(), " dilatih:", dilatih)
print("Rata-rata lapis Normalization:", np.round(norm.mean.numpy().ravel(), 3))
model.summary()