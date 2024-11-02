from tkinter import *

window = Tk()

def kgTogr():

    # Borrar el contenido anterior en las ventanas de texto
    b1.delete("1.0", END)
    b2.delete("1.0", END)
    b3.delete("1.0", END)

    # Convertir el valor de entrada y mostrarlo en las ventanas de texto
    gr = float(a1_value.get()) * 1000
    ps = float(a1_value.get()) * 2.20462
    os = float(a1_value.get()) * 35.274
    
    b1.insert(END, gr)
    b2.insert(END, ps)
    b3.insert(END, os)


a1_value = StringVar()
a1 = Entry(window, textvariable = a1_value)
a1.grid(row = 0, column = 0)

a2 = Label(window, text="kg")
a2.grid(row = 0, column = 1)

a3 = Button(window, text = "Convert", command = kgTogr )
a3.grid(row = 0, column = 2)

b1 = Text(window, height = 1, width = 20)
b1.grid(row = 1, column = 0)

b2 = Text(window, height = 1, width = 20)
b2.grid(row = 1, column = 1)

b3 = Text(window, height = 1, width = 20)
b3.grid(row = 1, column = 2)


window.mainloop()