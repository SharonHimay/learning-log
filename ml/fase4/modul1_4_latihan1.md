# Modul 1.4 - Latihan 1: Metrik dari Confusion Matrix

## Model deteksi kerusakan (TP=8, FP=2, FN=4, TN=86)

| Ukuran | Rumus | Hitungan | Hasil |
|--------|-------|----------|-------|
| Akurasi | (TP+TN)/total | (8+86)/100 | 0.94 |
| Precision | TP/(TP+FP) | 8/10 | 0.8 |
| Recall | TP/(TP+FN) | 8/12 | 0.667 |
| F1 | 2PR/(P+R) | 2 x 0.8 x 0.667 / (0.8+0.667) | 0.727 |
| Spesifisitas | TN/(TN+FP) | 86/88 | 0.977 |

## Model "selalu NORMAL"

- Akurasi = 88/100 = 0.88 (semua yang normal dijawab benar)
- Recall = 0/12 = 0 (tidak ada kerusakan yang ditemukan)
- Precision tidak terdefinisi (0/0), karena model tidak pernah memberi alarm

## Kesimpulan

Akurasi 0.94 dan 0.88 hanya berbeda 6 poin, padahal model pertama menemukan
8 dari 12 kerusakan dan model kedua tidak menemukan satu pun.