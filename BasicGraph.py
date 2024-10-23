from bokeh.plotting import figure
from bokeh.io import output_file, show

x = [1, 2, 3, 4, 6]
y = [4, 3, 7, 1, 12]

output_file("Line.html")

f = figure()

f.line(x, y)

show(f)