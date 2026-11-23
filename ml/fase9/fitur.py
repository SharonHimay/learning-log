import numpy as np
from data_imu import FS


def ekstrak_fitur(X):
    """X: (n, panjang, 3) -> fitur (n, 16)."""
    n, panjang, _ = X.shape
    fitur = []
    for sumbu in range(3):
        s = X[:, :, sumbu]
        fitur += [s.mean(axis=1), s.std(axis=1), s.min(axis=1), s.max(axis=1)]
    m = np.sqrt((X ** 2).sum(axis=2))                       # magnitudo
    fitur += [m.mean(axis=1), m.std(axis=1)]
    az = X[:, :, 2] - X[:, :, 2].mean(axis=1, keepdims=True)
    spektrum = np.abs(np.fft.rfft(az, axis=1))
    frek = np.fft.rfftfreq(panjang, d=1 / FS)
    spektrum[:, 0] = 0                                      # abaikan DC
    idx = spektrum.argmax(axis=1)
    fitur += [frek[idx], spektrum[np.arange(n), idx] / panjang]
    return np.stack(fitur, axis=1)


NAMA_FITUR = [f"{nama}_{s}" for s in ("ax", "ay", "az") for nama in ("mean", "std", "min", "max")] + \
             ["mag_mean", "mag_std", "frek_dom", "amp_dom"]