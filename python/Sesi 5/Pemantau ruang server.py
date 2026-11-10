def rata_rata (data):
    return round (sum(data) / len(data), 2)

def ringkasan (data):
    return min (data), max (data), rata_rata(data)

def status_ruang (suhu, kelembapan):
    if suhu > 35 or kelembapan > 80:
        return "BAHAYA"
    elif 28 <= suhu <= 35:
        return "WASPADA"
    else:
        return "AMAN"
    
data = [28.5, 30.1, 27.8, 31.4, 29.0]
terendah, tertinggi, rata = ringkasan (data)
print (terendah, tertinggi, rata)
print (status_ruang(30, 50))
print (status_ruang(25, 90))
print (status_ruang(25, 50))