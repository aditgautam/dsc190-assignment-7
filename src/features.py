import pandas as pd
from pathlib import Path

df = pd.read_csv("data/transformed/events.csv")

df["duration_minutes"] = df["duration_seconds"] / 60
df["weekday"] = pd.to_datetime(df["date"]).dt.day_name()

Path("data/features").mkdir(parents=True, exist_ok=True)
df.to_csv("data/features/events.csv", index=False)
