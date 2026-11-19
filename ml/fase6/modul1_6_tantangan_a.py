import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from zona import buat_data_zona


def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))


def loss_dan_gradien(parameter, X, y):
    """Loss (cross-entropy) dan gradiennya lewat backpropagation (aktivasi tanh)."""
    W1, b1, W2, b2 = parameter
    n = len(X)
    y = y.reshape(-1, 1)
    a1 = np.tanh(X @ W1 + b1)
    p = sigmoid(a1 @ W2 + b2)
    loss = float(-np.mean(y * np.log(p + 1e-12) + (1 - y) * np.log(1 - p + 1e-12)))

    dz2 = (p - y) / n
    dW2 = a1.T @ dz2
    db2 = dz2.sum(axis=0)
    dz1 = (dz2 @ W2.T) * (1 - a1 ** 2)
    dW1 = X.T @ dz1
    db1 = dz1.sum(axis=0)
    return loss, (dW1, db1, dW2, db2)


df = buat_data_zona()
X = df[["suhu", "kelembapan"]].to_numpy()
y = df["alarm"].to_numpy()
X_latih, _, y_latih, _ = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
X_s = StandardScaler().fit_transform(X_latih)

rng = np.random.default_rng(0)
parameter = [rng.normal(0, 0.5, (2, 4)), np.zeros(4), rng.normal(0, 0.5, (4, 1)), np.zeros(1)]
loss, gradien = loss_dan_gradien(parameter, X_s, y_latih)
print("Loss awal:", round(loss, 6))

eps = 1e-5
nama = ["W1", "b1", "W2", "b2"]
for k in range(4):
    analitik = gradien[k]
    numerik = np.zeros_like(parameter[k])
    it = np.nditer(parameter[k], flags=["multi_index"])
    for _ in it:
        idx = it.multi_index
        asli = parameter[k][idx]
        parameter[k][idx] = asli + eps
        loss_plus, _ = loss_dan_gradien(parameter, X_s, y_latih)
        parameter[k][idx] = asli - eps
        loss_minus, _ = loss_dan_gradien(parameter, X_s, y_latih)
        parameter[k][idx] = asli
        numerik[idx] = (loss_plus - loss_minus) / (2 * eps)
    selisih = np.max(np.abs(analitik - numerik)) / (np.max(np.abs(analitik) + np.abs(numerik)) + 1e-12)
    print(f"{nama[k]}: selisih relatif maksimum = {selisih:.2e}")

print("\nContoh W1[0,0]: analitik =", round(float(gradien[0][0, 0]), 8))