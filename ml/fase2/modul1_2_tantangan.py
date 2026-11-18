import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

from data_modul12 import buat_data

df = buat_data()
X = df[["suhu", "kelembapan"]]
y = df["status"]

skor_uji = []
for rs in range(10):
    X_latih, X_uji, y_latih, y_uji = train_test_split(
        X, y, test_size=0.2, random_state=rs, stratify=y)
    model = DecisionTreeClassifier(max_depth=2, random_state=42)
    model.fit(X_latih, y_latih)
    skor = model.score(X_uji, y_uji)
    skor_uji.append(skor)
    print(f"random_state={rs}: uji={skor:.3f}")

skor_uji = np.array(skor_uji)
print(f"min={skor_uji.min():.3f}  max={skor_uji.max():.3f}  "
      f"rata2={skor_uji.mean():.3f}  std={skor_uji.std():.3f}")