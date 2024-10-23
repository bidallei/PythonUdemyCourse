from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas as pd

df = pd.read_csv("data.csv")
x = df["x"]
y = df["y"]

output_file("Line_from_csv.html")

f = figure()

f.line(x, y)

show(f)