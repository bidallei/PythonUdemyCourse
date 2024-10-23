from bokeh.plotting import figure, output_file, show
import pandas as pd

df = pd.read_excel("https://github.com/pythonizing/data/raw/master/verlegenhuken.xlsx")
x = df["Temperature"]/10
y = df["Pressure"]/10

output_file("Line_from_excel.html")

r = figure()

r.title.text="Temperature and Air Pressure"
r.title.text_color="Gray"
r.title.text_font="arial"
r.title.text_font_style="bold"
r.xaxis.minor_tick_line_color=None
r.yaxis.minor_tick_line_color=None
r.xaxis.axis_label="Temperature (°C)"
r.yaxis.axis_label="Pressure (hPa)"   

r.line(x, y)

show(r)


