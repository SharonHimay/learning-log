# Modul 1.8 - Latihan 1: Konvolusi dan Pooling

## 1. Konvolusi 6x6 dengan filter tepi tegak [[-1,0,1],[-1,0,1],[-1,0,1]]

Gambar: tiga kolom kiri = 0, tiga kolom kanan = 1.

Hasil konvolusi (valid, 4x4), tiap baris sama:

    0  3  3  0

Perhitungan satu baris:
- Jendela kolom 0-2: (-1*0 + 0*0 + 1*0) x 3 baris = 0
- Jendela kolom 1-3: (-1*0 + 0*0 + 1*1) x 3 baris = 3
- Jendela kolom 2-4: (-1*0 + 0*1 + 1*1) x 3 baris = 3
- Jendela kolom 3-5: (-1*1 + 0*1 + 1*1) x 3 baris = 0

Setelah ReLU: tidak berubah (semua >= 0).
Setelah MaxPooling 2x2: [[3, 3], [3, 3]]

Gambar terbalik (kiri terang, kanan gelap): hasil konvolusi tiap baris
0 -3 -3 0. Setelah ReLU semuanya menjadi 0. Filter ini hanya "menyala"
untuk tepi gelap -> terang, bukan terang -> gelap.

## 2. Ukuran keluaran (rumus: floor((n - k + 2p) / s) + 1)

| Kasus | Hitungan | Hasil |
|-------|----------|-------|
| valid, stride 1 | (8-3)/1 + 1 | 6x6 |
| same, stride 1 | (8-3+2)/1 + 1 | 8x8 |
| valid, stride 2 | floor((8-3)/2) + 1 = floor(2.5) + 1 | 3x3 |

## 3. Parameter dan MAC

| Lapis | Parameter | MAC |
|-------|-----------|-----|
| Conv2D(8, 3, same) pada (8,8,1) | (3*3*1 + 1) * 8 = 80 | 8*8 * 9*1 * 8 = 4.608 |
| Conv2D(16, 3, same) pada (4,4,8) | (3*3*8 + 1) * 16 = 1.168 | 4*4 * 9*8 * 16 = 18.432 |

## 4. Dense vs Conv pada gambar 224x224x3

- Flatten: 224*224*3 = 150.528 nilai
- Dense(128): 150.528 * 128 + 128 = 19.267.712 parameter
- Conv2D(32, 3): (3*3*3 + 1) * 32 = 896 parameter
- Rasio: sekitar 21.500 kali