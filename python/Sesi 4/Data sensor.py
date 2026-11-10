sensors = [
    {"id": "ESP32-01", "suhu": 29.5, "kelembapan": 65},
    {"id": "ESP32-02", "suhu": 33.2, "kelembapan": 58},
    {"id": "ESP32-03", "suhu": 31.0, "kelembapan": 72},
]

# 1. Sensor dengan suhu > 30, sekaligus menjumlahkan suhu
print ("Sensor dengan suhu di atas 30: ")
total_suhu = 0
for s in sensors:
    if s["suhu"] > 30:
        print (s["id"])
    total_suhu += s["suhu"]
    
# 2. Rata-rata suhu
rata_rata = round (total_suhu / len(sensors), 2)
print ("Rata-rata suhu: ", rata_rata)

# 3. Tambah status, lalu tampilkan
for s in sensors:
    if s["suhu"] > 30:
        s["status"] = "PANAS"
    else:
        s["status"] = "NORMAL"
    print (s)