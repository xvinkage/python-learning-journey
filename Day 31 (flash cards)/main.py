from tkinter import *
from tkinter import messagebox
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pd.read_csv("data/words_to_learn.csv")
    print("Words to learn loaded")
except FileNotFoundError, pd.errors.EmptyDataError:
    data = pd.read_csv("data/french_words.csv")
    print("initial complete file loaded")


to_learn = data.to_dict(orient="records")
current_word = ""


def word_to_display():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    if len(to_learn) == 0:
        messagebox.showerror("Error", "You have completed all flashcards")
        return
    
    current_word = random.choice(to_learn)
    french_word = current_word["French"]
    card_canvas.itemconfig(card_title, text="French", fill= "black")
    card_canvas.itemconfig(card_word, text=french_word, fill= "black")
    card_canvas.itemconfig(front_card, image=card_front_img)
    flip_timer = window.after(3000, flip_card)

def flip_card():
    card_canvas.itemconfig(front_card, image=card_back_img)
    card_canvas.itemconfig(card_title, text="English", fill= "white")
    english_word = current_word["English"]
    card_canvas.itemconfig(card_word, text=english_word, fill= "white")

def wrong():
    word_to_display()

def right():
    to_learn.remove(current_word)
    df = pd.DataFrame(to_learn)
    df.to_csv("./data/words_to_learn.csv", mode="w", index=False)
    word_to_display()

def reset():
    global to_learn
    to_learn = data.to_dict(orient="records")
    df = pd.DataFrame(to_learn)
    df.to_csv("./data/words_to_learn.csv", index=False)
    word_to_display()


window = Tk()
window.configure(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flashy Cards")

flip_timer = window.after(3000, flip_card)


card_back_img = PhotoImage(file="./images/card_back.png")
card_canvas= Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
front_card = card_canvas.create_image(400, 263, image=card_front_img)
card_canvas.grid(row=0, column=0, columnspan=3)

card_title = card_canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = card_canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))


wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, borderwidth=0, command=wrong)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, highlightthickness=0, borderwidth=0, command=right)
right_button.grid(row=1, column=2)

reset_img = PhotoImage(file="./images/reset.png")
reset_button = Button(image=reset_img, highlightthickness=0, borderwidth=0, command=reset, bg=BACKGROUND_COLOR)
reset_button.grid(row=1, column=1)

word_to_display()


window.mainloop()
