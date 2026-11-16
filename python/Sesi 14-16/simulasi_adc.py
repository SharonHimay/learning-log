"""Simulasi ADC: kuantisasi sinus 5 Hz dan perhitungan SQNR."""
import numpy as np
import matplotlib.pyplot as plt

VREF = 3.3
FS = 1000          # laju sampling (Hz)
F_SINYAL = 5       # frekuensi sinus (Hz)

t = np.arange(0, 1, 1 / FS)
x = 1.65 + 1.65 * np.sin(2 * np.pi * F_SINYAL * t)    # 0 sampai 3,3 V penuh


def kuantisasi(x, n_bit):
    """Bulatkan tegangan ke 2**n_bit tingkat, kembalikan sebagai tegangan."""
    tingkat = 2 ** n_bit - 1
    kode = np.round(x / VREF * tingkat)
    return kode / tingkat * VREF


def sqnr_db(x, xq):
    daya_sinyal = np.var(x)
    daya_error = np.var(x - xq)
    return 10 * np.log10(daya_sinyal / daya_error)


print(f"{'N':>3} {'simulasi (dB)':>14} {'6,02N+1,76 (dB)':>16} {'selisih':>8}")
for n in (3, 4, 8, 12):
    xq = kuantisasi(x, n)
    sim = sqnr_db(x, xq)
    teori = 6.02 * n + 1.76
    print(f"{n:>3} {sim:>14.2f} {teori:>16.2f} {sim - teori:>8.2f}")

xq3 = kuantisasi(x, 3)
plt.plot(t, x, label="Sinyal asli")
plt.step(t, xq3, where="mid", label="Hasil kuantisasi 3-bit")
plt.xlabel("Waktu (s)")
plt.ylabel("Tegangan (V)")
plt.title("Kuantisasi ADC 3-bit")
plt.legend()
plt.grid(True)
plt.savefig("adc_3bit.png", dpi=120)
plt.show()