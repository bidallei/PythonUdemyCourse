from bokeh.plotting import figure, output_file, show
import pandas as pd
import yfinance as yf

# Obtener los datos de una acción desde Yahoo Finance (Adobe en este caso)
df = yf.download("ADBE", start="2024-01-01", end="2024-10-02")


p = figure(width = 500, height = 250, x_axis_type = "datetime", sizing_mode="stretch_both")

p.line(df.index, df["Close"], color="orange", alpha=0.5)

output_file("Timeseries.html")

show(p)