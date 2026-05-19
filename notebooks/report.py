import marimo

__generated_with = "0.23.6"
app = marimo.App()


@app.cell
def _():
    import pandas as pd
    import matplotlib.pyplot as plt
    import marimo as mo
    return mo, pd, plt


@app.cell
def _(pd):
    df = pd.read_csv("data/features/events.csv")
    return (df,)


@app.cell
def _(df, mo, plt):
    fig, ax = plt.subplots()
    ax.hist(df["duration_minutes"], bins=30, edgecolor="white")
    ax.set_title("Distribution of Event Durations")
    ax.set_xlabel("Duration (minutes)")
    ax.set_ylabel("Count")
    return mo.as_html(fig)


if __name__ == "__main__":
    app.run()
