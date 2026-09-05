from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)
# window.config(height=200, width=400)


def calc_km():
    user_input = textbox.get()
    km = float(user_input) * 1.60934
    result = round(km, 2)
    km_value.config(text=result)
    

textbox = Entry(width=7)
textbox.grid(row=0, column= 1)

miles_unit = Label(text="Miles")
miles_unit.grid(row= 0, column= 2)

equal_label = Label(text="is equal to")
equal_label.grid(row= 1, column= 0, pady= 10)

km_value = Label(text="0")
km_value.grid(row= 1, column= 1, pady=10)

km_unit = Label(text="Km")
km_unit.grid(row= 1, column= 2, pady= 10)

calc = Button(text="Calculate", command=calc_km)
calc.grid(row=2, column=1, pady= 0)




window.mainloop()