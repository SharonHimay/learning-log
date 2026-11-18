import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

folder = Path(__file__).parent
df = pd.read_csv(folder / "bersih.csv")

tabel = df.pivot_table(index="waktu", columns="sensor", values="suhu")
print(tabel.round(2))

print(df[["suhu", "kelembapan"]].corr())

tabel.plot(marker="o")
plt.ylabel("Suhu (°C)")
plt.title("Suhu tiga sensor per jam")
plt.show()