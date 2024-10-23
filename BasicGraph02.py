from bokeh.plotting import figure
from bokeh.io import output_file, show

x = [1, 4, 5, 8, 10]
y = [4, 3, 74, 16, 12]

output_file("Line.html")

f = figure()

f.circle_dot(x, y)

show(f)