import numpy as np

gambar = np.zeros((6, 6))
gambar[:, 3:] = 1
kernel = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])

keluar = np.zeros((4, 4))
for i in range(4):
    for j in range(4):
        keluar[i, j] = np.sum(gambar[i:i + 3, j:j + 3] * kernel)
print(keluar.astype(int))

relu = np.maximum(0, keluar)
pool = relu.reshape(2, 2, 2, 2).max(axis=(1, 3))
print(pool.astype(int))