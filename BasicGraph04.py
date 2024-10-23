from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas as pd

df = pd.read_csv("bachelors.csv")
x = df["Year"]
y = df["Engineering"]

output_file("Line_from_bachelor_csv.html")

f = figure()

f.line(x, y)

show(f)