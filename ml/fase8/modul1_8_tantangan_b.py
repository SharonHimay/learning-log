import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import keras
import numpy as np
from keras import layers

basis = keras.applications.MobileNetV2(
    input_shape=(96, 96, 3), alpha=0.35,
    include_top=False, weights=None)          # weights=None: hanya memeriksa struktur, tanpa unduhan
basis.trainable = False

masuk = keras.Input(shape=(96, 96, 3))
x = basis(masuk, training=False)
x = layers.GlobalAveragePooling2D()(x)
print("Bentuk keluaran GlobalAveragePooling2D:", x.shape)
x = layers.Dropout(0.2)(x)
keluaran = layers.Dense(10, activation="softmax")(x)
model = keras.Model(masuk, keluaran)

dilatih = int(sum(np.prod(w.shape) for w in model.trainable_weights))
dibekukan = int(sum(np.prod(w.shape) for w in model.non_trainable_weights))
print(f"Total={model.count_params():,}  dilatih={dilatih:,}  dibekukan={dibekukan:,}")
print(f"Porsi yang dilatih: {dilatih / model.count_params() * 100:.1f}%")
print("Keluaran basis:", basis.output_shape)