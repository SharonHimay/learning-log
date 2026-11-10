total = 0
for i in range (5):
    suhu = float(input(f"Suhu ke-{i + 1}: "))
    total += suhu
rata_rata = total / 5
print (f"Rata-rata: , {rata_rata}")