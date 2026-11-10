def minta_suhu():
    while True:
        try:
            suhu = float(input("Suhu (C): "))
        except ValueError:
            print("Harus berupa angka.")
            continue

        if -10 <= suhu <= 80:
            return suhu
        print("Di luar rentang -10 sampai 80.")

hasil = minta_suhu()
print("Diterima:", hasil)