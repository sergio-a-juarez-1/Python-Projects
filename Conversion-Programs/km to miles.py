from tkinter import *

window = Tk()
#window.minsize(300,200)
window.title("Celcius to Fahrenheit")


def calculate():
    kilometers = float(input.get())
    miles = kilometers * 0.621371
    result.config(text=f'{miles}')

input = Entry(width=7)
input.grid(row=0,column=1)

km = Label(text="Kilometers")
km.grid(row=0,column=2)

equal = Label(text="is equal to")
equal.grid(row=1, column=0)


result = Label(text='0')
result.grid(row=1,column=1)

mi = Label(text="Miles")
mi.grid(row=1,column=2)


button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)

window.mainloop()