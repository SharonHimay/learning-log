suhu = [28.5, 30.1, 27.8, 31.4, 29.0]

tertinggi = max(suhu)
terendah = min(suhu)
rata_rata = round(sum(suhu) / len(suhu), 2)

jumlah_di_atas_30 = 0
for s in suhu:
    if s > 30:
        jumlah_di_atas_30 += 1

print ("Tertinggi: ", tertinggi)
print ("Terendah: ", terendah)
print ("Rata-rata: ", rata_rata)
print ("Jumlah di atas 30:", jumlah_di_atas_30)