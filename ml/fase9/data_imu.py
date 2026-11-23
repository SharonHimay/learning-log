import numpy as np

FS = 50                                    # laju sampling (Hz), mirip MPU6050 di ESP32
KELAS = ["diam", "jalan", "lari", "goyang"]


def buat_rekaman(kelas, rng, detik=60):
    """Satu rekaman akselerometer 3 sumbu (satuan g), panjang detik*FS sampel."""
    n = detik * FS
    t = np.arange(n) / FS
    bias = rng.normal(0, 0.03, 3)                     # bias sensor tiap rekaman
    arah = rng.normal(0, 0.05, 2)                     # kemiringan sensor (gravitasi sedikit miring)
    if kelas == "diam":
        f, amp, noise = 1.0, 0.0, rng.uniform(0.03, 0.08)
    elif kelas == "jalan":
        f, amp, noise = rng.uniform(1.5, 2.6), rng.uniform(0.15, 0.5), rng.uniform(0.05, 0.14)
    elif kelas == "lari":
        f, amp, noise = rng.uniform(2.2, 3.4), rng.uniform(0.45, 1.1), rng.uniform(0.05, 0.14)
    else:  # goyang
        f, amp, noise = rng.uniform(3.0, 5.5), rng.uniform(0.25, 0.8), rng.uniform(0.08, 0.18)
    fase = rng.uniform(0, 2 * np.pi, 3)
    ax = arah[0] + 0.6 * amp * np.sin(2 * np.pi * f * t + fase[0])
    ay = arah[1] + 0.5 * amp * np.sin(2 * np.pi * f * t + fase[1])
    az = 1.0 + amp * np.sin(2 * np.pi * f * t + fase[2]) + 0.3 * amp * np.sin(2 * np.pi * 2 * f * t)
    sinyal = np.stack([ax, ay, az], axis=1) + bias + rng.normal(0, noise, (n, 3))
    return sinyal.astype("float32")


def buat_data_imu(rekaman_per_kelas=8, seed=11):
    """Daftar rekaman: (id, label, sinyal)."""
    rng = np.random.default_rng(seed)
    data = []
    id_rekaman = 0
    for label, kelas in enumerate(KELAS):
        for _ in range(rekaman_per_kelas):
            data.append((id_rekaman, label, buat_rekaman(kelas, rng)))
            id_rekaman += 1
    return data


def buat_jendela(data, panjang=100, langkah=50):
    """Potong tiap rekaman menjadi jendela. Kembalikan X (n, panjang, 3), y, grup (id rekaman)."""
    X, y, g = [], [], []
    for id_rekaman, label, sinyal in data:
        for awal in range(0, len(sinyal) - panjang + 1, langkah):
            X.append(sinyal[awal:awal + panjang])
            y.append(label)
            g.append(id_rekaman)
    return np.array(X), np.array(y), np.array(g)