from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# 
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    pass_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get().lower()
    username = username_entry.get()
    password = pass_entry.get()
    entry = {
        website: {
            "email": username,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Please do not leave any fields empty")
    else:
        confirmation = messagebox.askokcancel(title=website, message=f"These are the details entered website:{website} email:{username} password:{password} \n Would you like to save?")
        if confirmation:

            try:

                with open("data.json", "r") as data_file:
                #read old data
                    data = json.load(data_file)
                    data.update(entry)
                with open("data.json", "w") as data_file: 
                    json.dump(data, data_file, indent=4)

            except FileNotFoundError:
                with open("data.json", "w") as data_file: 
                    json.dump(entry, d_file, indent=4)

            pass_entry.delete(0, "end")
            website_entry.delete(0, "end")
            messagebox.showinfo(title="Confirmation", message="Succesfully saved")

def find_password():
    user_search = website_entry.get().lower()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
    else:
        try:
            found_passataword = data[user_search]
            messagebox.showinfo(title="Search Results", message=f"Site: {user_search}\nEmail: {found_password["email"]}\nPassword: {found_password["password"]}")
            
        except KeyError:
            messagebox.showerror(title="Error", message="Site not found")
    

# ---------------------------- UI SETUP --------------------


window = Tk()

window.config(padx=50, pady=50)
window.minsize(height= 300, width=100)
window.title("Password Manager")

logo = PhotoImage(file="logo.png")
logo_img = Label(image=logo)
logo_img.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry()
website_entry.grid(row=1, column=1, columnspan=1, sticky=EW)
website_entry.focus()


username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)


username_entry = Entry()
username_entry.grid(row=2, column=1, columnspan=2, sticky=EW)
username_entry.insert(0,"user@gmail.com")

pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)

pass_entry = Entry()
pass_entry.grid(row=3, column=1, sticky=EW)


gen_pass = Button(text="Generate Password", command=gen_password)
gen_pass.grid(row=3, column=2, sticky=EW)


add_pass = Button(text="Add", command=save)
add_pass.grid(row=4, column=1, columnspan=2, sticky=EW)

search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1, sticky=EW)

window.mainloop()
