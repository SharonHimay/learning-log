import numpy as np

t = np.linspace(0, 1, 500)
sinyal = np.sin(2 * np.pi * 5 * t)

np.random.seed(0)
for sigma in [0.1, 0.5, 1.0]:
    noise = np.random.normal(0, sigma, size=t.shape)
    rasio = np.mean(sinyal ** 2) / np.mean(noise ** 2)
    print(f"noise {sigma}: rasio {rasio:.2f}, {10 * np.log10(rasio):.1f} dB")