import pandas as pd
from pathlib import Path

df = pd.read_csv("data/clean/events.csv")

df["date"] = pd.to_datetime(df["timestamp"]).dt.strftime("%Y-%m-%d")

Path("data/transformed").mkdir(parents=True, exist_ok=True)
df.to_csv("data/transformed/events.csv", index=False)
