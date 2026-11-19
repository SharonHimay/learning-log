import numpy as np


def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))


def bce(p, y):
    eps = 1e-12
    return float(-np.mean(y * np.log(p + eps) + (1 - y) * np.log(1 - p + eps)))


def latih_neuron(X, y, lr=0.1, epoch=500):
    """Satu neuron + sigmoid (= regresi logistik) dengan gradient descent."""
    n, d = X.shape
    w = np.zeros(d)
    b = 0.0
    riwayat = []
    for e in range(epoch):
        p = sigmoid(X @ w + b)
        riwayat.append(bce(p, y))
        dz = (p - y) / n              # turunan loss terhadap z
        w -= lr * (X.T @ dz)
        b -= lr * dz.sum()
    return w, b, riwayat

def fungsi_aktivasi(z, aktivasi):
    return np.maximum(0, z) if aktivasi == "relu" else np.tanh(z)


def turunan_aktivasi(z, a, aktivasi):
    return (z > 0).astype(float) if aktivasi == "relu" else 1 - a ** 2


def inisialisasi(d, hidden, seed):
    rng = np.random.default_rng(seed)
    return [
        rng.normal(0, 1, (d, hidden)) * np.sqrt(2.0 / d),
        np.zeros(hidden),
        rng.normal(0, 1, (hidden, 1)) * np.sqrt(2.0 / hidden),
        np.zeros(1),
    ]


def maju(parameter, X, aktivasi):
    W1, b1, W2, b2 = parameter
    z1 = X @ W1 + b1
    a1 = fungsi_aktivasi(z1, aktivasi)
    p = sigmoid(a1 @ W2 + b2).ravel()
    return z1, a1, p


def loss_dan_gradien(parameter, X, y, aktivasi="tanh"):
    W1, b1, W2, b2 = parameter
    n = X.shape[0]
    z1, a1, p = maju(parameter, X, aktivasi)
    loss = bce(p, y)
    dz2 = (p - y).reshape(-1, 1) / n
    dW2 = a1.T @ dz2
    db2 = dz2.sum(axis=0)
    dz1 = (dz2 @ W2.T) * turunan_aktivasi(z1, a1, aktivasi)
    dW1 = X.T @ dz1
    db1 = dz1.sum(axis=0)
    return loss, [dW1, db1, dW2, db2]


def latih_jaringan(X, y, hidden=4, lr=0.5, epoch=3000, seed=0, aktivasi="relu"):
    parameter = inisialisasi(X.shape[1], hidden, seed)
    riwayat = []
    for _ in range(epoch):
        loss, grad = loss_dan_gradien(parameter, X, y, aktivasi)
        riwayat.append(loss)
        for par, g in zip(parameter, grad):
            par -= lr * g
    return parameter, riwayat


def prediksi_jaringan(parameter, X, aktivasi="relu"):
    """Mengembalikan peluang kelas 1 untuk tiap baris X."""
    return maju(parameter, X, aktivasi)[2]
