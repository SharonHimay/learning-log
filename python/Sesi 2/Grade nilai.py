nilai = float(input("Nilai (0-100): "))

if nilai < 0 or nilai > 100:
    print ("Nilai tidak valid")
elif nilai >= 85:
    print ("A")
elif nilai >= 70:
    print ("B")
elif nilai >= 55:
    print ("C")
else:
    print ("D")