suhu = float(input ("Suhu (C): "))
kelembapan = float(input("Kelembapan (%): "))

if suhu > 35 or kelembapan > 80:
    print ("BAHAYA")
elif 28 <= suhu <= 35:
    print ("WASPADA")
else:
    print ("AMAN")