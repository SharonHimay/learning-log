import numpy as np
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.tree import DecisionTreeClassifier

from data_modul12 import buat_data

df = buat_data()
y = df["status"]
X = df[["suhu", "kelembapan"]]

X_latih, X_uji, y_latih, y_uji = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

print("=== Langkah 1: kedalaman pohon ===")
for d in [1, 2, 3, 5, 10, None]:
    model = DecisionTreeClassifier(max_depth=d, random_state=42)
    model.fit(X_latih, y_latih)
    print(f"depth={str(d):>4}  latih={model.score(X_latih, y_latih):.3f}  "
          f"uji={model.score(X_uji, y_uji):.3f}  daun={model.get_n_leaves()}")

print("\n=== Langkah 2: cross-validation 5-fold ===")
for d in [1, 2, 3, 5, None]:
    model = DecisionTreeClassifier(max_depth=d, random_state=42)
    skor = cross_val_score(model, X, y, cv=5)
    print(f"depth={str(d):>4}  rata2={skor.mean():.3f}  std={skor.std():.3f}")

print("\n=== Langkah 3: hanya fitur kelembapan ===")
X1 = df[["kelembapan"]]
X1_latih, X1_uji, y1_latih, y1_uji = train_test_split(
    X1, y, test_size=0.2, random_state=42, stratify=y)
for d in [1, 3, None]:
    model = DecisionTreeClassifier(max_depth=d, random_state=42)
    model.fit(X1_latih, y1_latih)
    print(f"depth={str(d):>4}  latih={model.score(X1_latih, y1_latih):.3f}  "
          f"uji={model.score(X1_uji, y1_uji):.3f}")