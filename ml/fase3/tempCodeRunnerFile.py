
print("Kelas      :", model.classes_)
print("Koefisien  :", model.coef_[0].round(4))
print("Intercept  :", model.intercept_.round(4))
print("Akurasi latih:", round(model.score(X_latih, y_latih), 3))
print("Akurasi uji  :", round(model.score(X_uji, y_uji), 3))

# 2. Pembanding
baseline = DummyClassifier(strategy="most_frequent").fit(X_latih, y_latih)
pohon = DecisionTreeClassifier(max_depth=2, random_state=42).fit(X_latih, y_latih)
print("\nBaseline uji:", round(baseline.score(X_uji, y_uji), 3))
print("Pohon depth=2 uji:", round(pohon.score(X_uji, y_uji), 3))
