import numpy as np
import matplotlib.pyplot as plt

dbm = np.arange(-30, 31, 5)
mw = 10 ** (dbm / 10)

# Gambar 1: sumbu y biasa
plt.figure()
plt.plot(dbm, mw, marker="o")
plt.xlabel("Daya (dBm)")
plt.ylabel("Daya (mW)")
plt.title("dBm ke mW (skala linear)")
plt.grid(True)
plt.savefig("dbm_linear.png", dpi=150)
plt.show()

# Gambar 2: sumbu y logaritmik
plt.figure()
plt.plot(dbm, mw, marker="o")
plt.yscale("log")
plt.xlabel("Daya (dBm)")
plt.ylabel("Daya (mW)")
plt.title("dBm ke mW (skala log)")
plt.grid(True)
plt.savefig("dbm_log.png", dpi=150)
plt.show()