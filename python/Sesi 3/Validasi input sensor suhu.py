while True:
    suhu = float(input("Suhu (C): "))
    if -10 <= suhu <= 80:
        print (f"Suhu diterima: {suhu}")
        break
    print ("Pembacaan sensor tidak valid, ulangi.")