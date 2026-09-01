from tkinter import *

window = Tk()
#window.minsize(300,200)
window.title("Celcius to Fahrenheit")


def calculate():
    fahrenheit = float(input.get())
    celcius = round((fahrenheit-32) * 5/9, 2)
    result.config(text=f'{celcius}')

input = Entry(width=7)
input.grid(row=0,column=1)

f = Label(text="Fahrenheit")
f.grid(row=0,column=2)

equal = Label(text="is equal to")
equal.grid(row=1, column=0)


result = Label(text='0')
result.grid(row=1,column=1)

c = Label(text="Celcius")
c.grid(row=1,column=2)


button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)

window.mainloop()