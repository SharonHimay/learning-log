import random
from datetime import datetime

# 1. Tulis log.csv (header + 5 data)
with open("log.csv", "w") as f:
    f.write("waktu,suhu\n")
    for i in range(5):
        suhu = round(random.uniform(25, 35), 1)
        waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{waktu},{suhu}\n")

# 2 dan 3. Baca lagi, lewati header, hitung rata-rata
try:
    with open("log.csv", "r") as f:
        semua_baris = f.readlines()

    total = 0
    for baris in semua_baris[1:]:
        bagian = baris.strip().split(",")
        total += float(bagian[1])

    jumlah_data = len(semua_baris) - 1
    print("Rata-rata suhu:", round(total / jumlah_data, 2))
except FileNotFoundError:
    print("log.csv tidak ditemukan.")