from sklearn.dummy import DummyClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import MinMaxScaler, StandardScaler

from data_modul15 import buat_data_motor

df = buat_data_motor()
print("Bentuk:", df.shape)
print("Kondisi:", df["kondisi"].value_counts().to_dict())
print("Data kosong:", df.isna().sum()[["arus_ma", "suhu_motor"]].to_dict())
print(df[["getaran", "arus_ma", "suhu_motor"]].describe().round(2))

X = df[["getaran", "arus_ma", "suhu_motor"]]
y = df["kondisi"]
X_latih, X_uji, y_latih, y_uji = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y)
print("\nUkuran latih/uji:", X_latih.shape, X_uji.shape)

baseline = DummyClassifier(strategy="most_frequent").fit(X_latih, y_latih)
print("Baseline uji:", baseline.score(X_uji, y_uji))

isi = lambda: SimpleImputer(strategy="median")
model_model = {
    "KNN tanpa skala": make_pipeline(isi(), KNeighborsClassifier(5)),
    "KNN + StandardScaler": make_pipeline(isi(), StandardScaler(), KNeighborsClassifier(5)),
    "KNN + MinMaxScaler": make_pipeline(isi(), MinMaxScaler(), KNeighborsClassifier(5)),
    "Logistik tanpa skala": make_pipeline(isi(), LogisticRegression(max_iter=1000)),
    "Logistik + StandardScaler": make_pipeline(isi(), StandardScaler(), LogisticRegression()),
}

print()
for nama, model in model_model.items():
    model.fit(X_latih, y_latih)
    cv = cross_val_score(model, X, y, cv=5)
    print(f"{nama:<28} uji={model.score(X_uji, y_uji):.3f}  "
          f"CV={cv.mean():.3f} (std {cv.std():.3f})")