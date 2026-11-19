# Modul 1.5 - Latihan 1: Skala dan Encoding

## Data: [26.5, 28.0, 25.0, 31.4, 29.0]

- min = 25.0, max = 31.4, rentang = 6.4
- rata-rata = 27.98, simpangan baku populasi = 2.182

| Nilai | Min-max | Z-score |
|-------|---------|---------|
| 26.5 | (26.5-25)/6.4 = 0.234 | (26.5-27.98)/2.182 = -0.678 |
| 28.0 | 0.469 | 0.009 |
| 25.0 | 0.0 | -1.366 |
| 31.4 | 1.0 | 1.567 |
| 29.0 | 0.625 | 0.467 |

## Data baru 33.0 (parameter dari data di atas, TIDAK dihitung ulang)

- Min-max: (33-25)/6.4 = 1.25 (di atas 1, wajar untuk data baru)
- Z-score: (33-27.98)/2.182 = 2.301

## Jenis encoding

| Kolom | Jenis | Encoding |
|-------|-------|----------|
| lokasi (lab, gudang, luar) | Nominal, tanpa urutan | One-hot |
| beban (rendah, sedang, tinggi) | Ordinal, ada urutan | Ordinal (0, 1, 2) |
| id_sensor (A, B, C) | Nominal, tanpa urutan | One-hot |

## One-hot lokasi (urutan alfabet: gudang, lab, luar)

| Nilai | gudang | lab | luar |
|-------|--------|-----|------|
| lab | 0 | 1 | 0 |
| gudang | 1 | 0 | 0 |
| luar | 0 | 0 | 1 |