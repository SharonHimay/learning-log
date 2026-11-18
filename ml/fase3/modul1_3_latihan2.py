import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score, train_test_split

from data_modul13 import buat_data_cpu

df = buat_data_cpu()
X = df[["beban_cpu", "suhu_ruang"]]
y = df["suhu_cpu"]
X_latih, X_uji, y_latih, y_uji = train_test_split(
    X, y, test_size=0.2, random_state=42)

model = LinearRegression().fit(X_latih, y_latih)
pred = model.predict(X_uji)

print("=== Model linear (data uji) ===")
print("MAE :", round(mean_absolute_error(y_uji, pred), 3))
print("RMSE:", round(np.sqrt(mean_squared_error(y_uji, pred)), 3))
print("R2  :", round(r2_score(y_uji, pred), 3))

baseline = DummyRegressor(strategy="mean").fit(X_latih, y_latih)
pred_dasar = baseline.predict(X_uji)
print("\n=== Baseline (rata-rata) ===")
print("MAE :", round(mean_absolute_error(y_uji, pred_dasar), 3))
print("RMSE:", round(np.sqrt(mean_squared_error(y_uji, pred_dasar)), 3))
print("R2  :", round(r2_score(y_uji, pred_dasar), 3))

print("\nR2 data latih:", round(model.score(X_latih, y_latih), 3))
skor = cross_val_score(LinearRegression(), X, y, cv=5, scoring="r2")
print("CV R2:", skor.round(3), "rata-rata", round(skor.mean(), 3))

print("\nPrediksi beberapa input:")
for beban, ruang in [(0, 27), (50, 27), (100, 27), (50, 33)]:
    baru = pd.DataFrame([[beban, ruang]], columns=X.columns)
    print(f"beban={beban:>3} suhu_ruang={ruang} -> {float(model.predict(baru)[0]):.2f}")

plt.scatter(y_uji, pred)
batas = [y_uji.min(), y_uji.max()]
plt.plot(batas, batas, "r--", label="Prediksi sempurna")
plt.xlabel("Suhu CPU sebenarnya (C)")
plt.ylabel("Suhu CPU prediksi (C)")
plt.title("Regresi linear: sebenarnya vs prediksi")
plt.legend()
plt.grid(True)
plt.savefig("sebenarnya_vs_prediksi.png", dpi=120)
plt.show()