def add(*args):
    for i in args:
        return sum(args)

print(add(1, 3, 5, 5))

# import tkinter

# window = tkinter.Tk()
# window.title("BAMN Systems")
# window.minsize(width=500, height=300)
# window.config(padx= 100, pady=200)

# # click = 0
# def button_click():
#     # global click
#     # click+=1
#     get= input.get()

#     label["text"] = f"Clicked {get} times"
#     print("I got clicked")


# label = tkinter.Label(text="This is a label", font=("Courier", 12, "bold"))
# label.grid(column=0, row=0)
# label.config(padx = 50, pady = 50)
# # label.pack()


# button = tkinter.Button(text= "Click Me!", command= button_click)
# button.grid(column=1, row=1)

# new_button= tkinter.Button(text="This does not work")
# new_button.grid(column=2, row= 0)


# input = tkinter.Entry(width= 10)
# input.grid(column=3, row= 2)
# # input.pack()

# window.mainloop()