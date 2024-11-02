'''
A program that stores this book information:
- Title
- Author
- Year
- ISBN

User can:
- View all records
- Search an entry
- Add an entry
- Update entry
- Delete
- Close

'''

from tkinter import *

window = Tk()

def kgTogr():

    # Borrar el contenido anterior en las ventanas de texto
    b1.delete("1.0", END)
    b2.delete("1.0", END)
    b3.delete("1.0", END)

    # Convertir el valor de entrada y mostrarlo en las ventanas de texto
    gr = float(a2_value.get()) * 1000
    ps = float(a2_value.get()) * 2.20462
    os = float(a2_value.get()) * 35.274
    
    b1.insert(END, gr)
    b2.insert(END, ps)
    b3.insert(END, os)

a1 = Label(window, text = "Title")
a1.grid(row = 0, column = 0)

a2_value = StringVar()
a2 = Entry(window, textvariable = a2_value)
a2.grid(row = 0, column = 1)

a3 = Label(window, text = "Author")
a3.grid(row = 0, column = 2)

a4_value = StringVar()
a4 = Entry(window, textvariable = a4_value)
a4.grid(row = 0, column = 3)

b1 = Label(window, text = "Year")
b1.grid(row = 1, column = 0)

b2_value = StringVar()
b2 = Entry(window, textvariable = b2_value)
b2.grid(row = 1, column = 1)

b3 = Label(window, text = "ISBN")
b3.grid(row = 1, column = 2)

b4_value = StringVar()
b4 = Entry(window, textvariable = b4_value)
b4.grid(row = 1, column = 3)

c1 = Text(window, height = 6, width = 40)
c1.grid(row = 2, rowspan = 7 , column = 0,  columnspan = 3)

c3 = Button(window, text = "View all", command = kgTogr )
c3.grid(row = 2, column = 3)

d3 = Button(window, text = "Search entry", command = kgTogr )
d3.grid(row = 3, column = 3)

e3 = Button(window, text = "Add entry", command = kgTogr )
e3.grid(row = 4, column = 3)

f3 = Button(window, text = "Update", command = kgTogr )
f3.grid(row = 5, column = 3)

g3 = Button(window, text = "Delete", command = kgTogr )
g3.grid(row = 6, column = 3)

h3 = Button(window, text = "Close", command = kgTogr )
h3.grid(row = 7, column = 3)


window.mainloop()