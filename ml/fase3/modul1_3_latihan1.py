import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

from data_modul13 import buat_data_cpu

df = buat_data_cpu()
print("Bentuk:", df.shape)
print(df.describe().round(2))

X = df[["beban_cpu", "suhu_ruang"]]
y = df["suhu_cpu"]

X_latih, X_uji, y_latih, y_uji = train_test_split(
    X, y, test_size=0.2, random_state=42)
print("\nUkuran latih/uji:", X_latih.shape, X_uji.shape)

model = LinearRegression()
model.fit(X_latih, y_latih)
print("Koefisien:", model.coef_.round(4))
print("Intercept:", round(model.intercept_, 4))

# Prediksi manual vs model
beban, suhu_ruang = 80, 30
manual = model.intercept_ + model.coef_[0] * beban + model.coef_[1] * suhu_ruang
baru = pd.DataFrame([[beban, suhu_ruang]], columns=X.columns)
print("\nPrediksi manual :", round(manual, 3))
print("Prediksi model  :", round(float(model.predict(baru)[0]), 3))
manual_bulat = 12.7433 + 0.2816 * beban + 0.9288 * suhu_ruang
print("Manual (koefisien dibulatkan):", round(manual_bulat, 4))