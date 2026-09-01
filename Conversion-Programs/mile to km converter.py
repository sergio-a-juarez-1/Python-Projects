from tkinter import *

window = Tk()
#window.minsize(300,200)
window.title("Mile to Km Converter")


def calculate():
    mile = float(input.get())
    kilometer = round(mile * 1.60934,2)
    result.config(text=f'{kilometer}')

input = Entry(width=7)
input.grid(row=0,column=1)

miles = Label(text="Miles")
miles.grid(row=0,column=2)

equal = Label(text="is equal to")
equal.grid(row=1, column=0)


result = Label(text='0')
result.grid(row=1,column=1)

km = Label(text="Km")
km.grid(row=1,column=2)


button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)

window.mainloop()