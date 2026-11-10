import os

folder = os.path.dirname(os.path.abspath(__file__))
nama_file = os.path.join(folder, "suhu.txt")

try:
    data = []
    with open(nama_file, "r") as f:
        for baris in f:
            baris = baris.strip()
            if baris:                      # lewati baris kosong
                data.append(float(baris))

    if data:
        print("Jumlah data:", len(data))
        print("Tertinggi:", max(data))
        print("Rata-rata:", round(sum(data) / len(data), 2))
    else:
        print("File kosong, tidak ada data yang bisa dihitung.")
except FileNotFoundError:
    print(f"File '{nama_file}' tidak ditemukan, cek nama dan foldernya.")