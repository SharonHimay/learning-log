import sys
from pathlib import Path

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, classification_report, confusion_matrix,
    f1_score, precision_score, recall_score, roc_auc_score,
)
from sklearn.model_selection import train_test_split

sys.path.append(str(Path(__file__).parent.parent / "fase2"))
from data_modul12 import buat_data # type: ignore

df = buat_data()
X = df[["suhu", "kelembapan"]]
y = df["status"]
X_latih, X_uji, y_latih, y_uji = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = LogisticRegression().fit(X_latih, y_latih)
p_panas = model.predict_proba(X_uji)[:, 1]   # kolom 1 = peluang PANAS

for ambang in [0.5, 0.3, 0.7]:
    pred = np.where(p_panas >= ambang, "PANAS", "NORMAL")
    print(f"--- ambang {ambang} ---")
    print(confusion_matrix(y_uji, pred, labels=["NORMAL", "PANAS"]))
    print("akurasi  :", round(accuracy_score(y_uji, pred), 3))
    print("precision:", round(precision_score(y_uji, pred, pos_label="PANAS"), 3))
    print("recall   :", round(recall_score(y_uji, pred, pos_label="PANAS"), 3))
    print("F1       :", round(f1_score(y_uji, pred, pos_label="PANAS"), 3))

print(classification_report(y_uji, model.predict(X_uji)))
print("AUC:", round(roc_auc_score(y_uji == "PANAS", p_panas), 3))