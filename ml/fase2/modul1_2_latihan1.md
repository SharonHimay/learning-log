# Modul 1.2 - Latihan 1: Mengenali Jenis Masalah

## Tabel jenis masalah

| # | Kasus | Jenis | Tugas | Fitur | Label |
|---|-------|-------|-------|-------|-------|
| 1 | Suhu ruangan 1 jam ke depan | Supervised | Regresi | Suhu 24 jam terakhir | Suhu 1 jam ke depan |
| 2 | Kata "ya" atau "tidak" | Supervised | Klasifikasi | Ciri sinyal suara | "ya" atau "tidak" |
| 3 | Mengelompokkan data getaran | Unsupervised | Clustering | - | - |
| 4 | Arus mesin tidak biasa | Unsupervised | Deteksi anomali | - | - |
| 5 | Sisa umur baterai | Supervised | Regresi | Tegangan, suhu | Sisa umur (jam) |
| 6 | Foto berisi orang atau tidak | Supervised | Klasifikasi | Piksel foto | Ada orang / tidak |

## Pertanyaan konsep

**(a) Kenapa akurasi tidak boleh diukur pada data latih?**
Model bisa menghafal data latih, jadi skor tinggi tidak membuktikan ia paham.

**(b) Apa itu data leakage?**
Informasi dari data uji bocor ke proses pelatihan, misalnya menghitung rata-rata
dari seluruh data sebelum membagi.

**(c) Kenapa stratify berguna?**
Menjaga proporsi kelas sama di data latih dan data uji.