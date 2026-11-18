import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

folder = Path(__file__).parent
df = pd.read_csv(folder / "bersih.csv")

data = {
    "waktu": ["08:00", "08:00", "08:00", "09:00", "09:00", "09:00",
              "10:00", "10:00", "10:00", "11:00", "11:00", "11:00"],
    "sensor": ["A", "B", "C"] * 4,
    "suhu": [26.5, 28.0, 25.0, 27.2, 29.1, None, 29.0, 31.4, 27.5, 30.2, 33.0, 28.0],
    "kelembapan": [60, 55, 70, 58, 52, 68, 55, 50, None, 52, 48, 66],
}
df = pd.DataFrame(data)
df.to_csv("sensor.csv", index=False)
print("sensor.csv dibuat:", df.shape)