from sklearn.dummy import DummyClassifier
from sklearn.model_selection import train_test_split

from data_modul12 import buat_data

df = buat_data()
X = df[["suhu", "kelembapan"]]
y = df["status"]

# Pembagian 80/20 dengan stratify
X_latih, X_uji, y_latih, y_uji = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

print("Bentuk:", X_latih.shape, X_uji.shape, y_latih.shape, y_uji.shape)
print("Proporsi data latih:")
print(y_latih.value_counts(normalize=True).round(3))
print("Proporsi data uji:")
print(y_uji.value_counts(normalize=True).round(3))

# Baseline
baseline = DummyClassifier(strategy="most_frequent")
baseline.fit(X_latih, y_latih)
print("Akurasi baseline (uji):", round(baseline.score(X_uji, y_uji), 3))

# Tanpa stratify
_, _, y_latih2, y_uji2 = train_test_split(X, y, test_size=0.2, random_state=42)
print("\nTanpa stratify, proporsi latih:", y_latih2.value_counts(normalize=True).round(3).to_dict())
print("Tanpa stratify, proporsi uji  :", y_uji2.value_counts(normalize=True).round(3).to_dict())

# Tiga bagian 60/20/20
X_sisa, X_uji3, y_sisa, y_uji3 = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)
X_lat3, X_val3, y_lat3, y_val3 = train_test_split(
    X_sisa, y_sisa, test_size=0.25, random_state=42, stratify=y_sisa)
print("\nUkuran latih/validasi/uji:", len(X_lat3), len(X_val3), len(X_uji3))