# Modul 1.9 - Latihan 1: Windowing dan Fitur

## 1. Jumlah jendela (rumus: floor((N - W) / S) + 1, N = 3000)

| W | S | Hitungan | Jendela |
|---|---|----------|---------|
| 100 | 50 | (3000-100)/50 + 1 | 59 |
| 100 | 25 | (3000-100)/25 + 1 | 117 |
| 100 | 100 | (3000-100)/100 + 1 | 30 |
| 200 | 50 | (3000-200)/50 + 1 | 57 |
| 50 | 25 | (3000-50)/25 + 1 | 119 |

## 2. Parameter sinyal (fs = 50 Hz)

- Durasi jendela 100 sampel = 100/50 = 2 detik
- Resolusi frekuensi (fs/W): W=50 -> 1,0 Hz; W=100 -> 0,5 Hz; W=200 -> 0,25 Hz
- Buffer 100 x 3 sampel: float32 = 100*3*4 = 1.200 byte; int16 = 600 byte
- Nyquist untuk 5,5 Hz: fs >= 2 * 5,5 = 11 Hz (50 Hz sangat cukup)

## 3. Jendela [0.9, 1.1, 1.3, 0.7]

- Rata-rata = (0.9+1.1+1.3+0.7)/4 = 1.0
- Simpangan baku populasi = sqrt((0.01+0.01+0.09+0.09)/4) = sqrt(0.05) = 0.2236
- Minimum = 0.7, maksimum = 1.3
- RMS = sqrt((0.81+1.21+1.69+0.49)/4) = sqrt(1.05) = 1.0247
- Rata-rata dikurangkan: [-0.1, 0.1, 0.3, -0.3]
  Tanda: -, +, +, -  -> berubah tanda 2 kali dari 3 selang = 2 persilangan nol

## 4. Conv1D

| Lapis | Parameter | MAC |
|-------|-----------|-----|
| Conv1D(8, 5, same) pada (100, 3) | (5*3 + 1) * 8 = 128 | 100 * 5 * 3 * 8 = 12.000 |
| Conv1D(16, 5, same) pada (50, 8) | (5*8 + 1) * 16 = 656 | 50 * 5 * 8 * 16 = 32.000 |