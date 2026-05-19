import pandas as pd
from pathlib import Path

VALID_EVENT_TYPES = {"click", "login", "purchase", "scroll", "view"}

df = pd.read_csv("data/raw/events.csv")

df = df.dropna()

df = df[df["event_type"].isin(VALID_EVENT_TYPES)]

df = df[df["duration_seconds"] > 0]

df["timestamp"] = pd.to_datetime(df["timestamp"], format="mixed").dt.strftime("%Y-%m-%dT%H:%M:%S")

Path("data/clean").mkdir(parents=True, exist_ok=True)
df.to_csv("data/clean/events.csv", index=False)
