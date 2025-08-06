import marimo

__generated_with = "0.10.16"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import polars as pl
    import plotly as px
    return mo, pl, px


@app.cell
def _(pl):
    journey = pl.read_csv(
        'data/customer_journey_utf_8.csv',
        skip_rows = 12,
        schema_overrides = {
            "Parent ID" : pl.String
        }
    )
    return (journey,)


@app.cell
def _(journey):
    journey.describe()
    return


if __name__ == "__main__":
    app.run()
