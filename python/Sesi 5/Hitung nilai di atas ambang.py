def hitung_di_atas (data, ambang = 30):
    jumlah = 0
    for nilai in data:
        if nilai > ambang:
            jumlah += 1
    return jumlah

data = [28.5, 30.1, 27.8, 31.4, 29.0]
print(hitung_di_atas(data))        # 2
print(hitung_di_atas(data, 28))    # 4