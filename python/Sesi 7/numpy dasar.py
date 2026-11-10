import numpy as np

suhu = np.array([28.5, 30.1, 27.8, 31.4, 29.0])

fahrenheit = np.round(suhu * 9 / 5 + 32, 2)
print("Fahrenheit:", fahrenheit)
print("Tertinggi:", np.max(suhu))
print("Terendah:", np.min(suhu))
print("Rata-rata:", round(np.mean(suhu), 2))
print("Jumlah di atas 30:", np.sum(suhu > 30))
print("Nilai di atas 30:", suhu[suhu > 30])