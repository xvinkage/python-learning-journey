from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global REPS
    window.after_cancel(timer)
    checkmarks["text"]= ""
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    REPS = 0
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():

    global REPS

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    REPS +=1

    if REPS % 2 != 0:
    #1, 3 5
        countdown(work_sec)
        timer_label.config(text ="Work")
    elif REPS % 8 == 0:
    # 8
        countdown(long_break_sec)
        timer_label.config(text ="Long Break", fg=RED)

    elif REPS % 2 == 0:
        #2nd 4th, 6th
        countdown(short_break_sec)
        timer_label.config(text ="Short Break", fg=PINK)
        checkmarks["text"]+= "✓"

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def countdown(count):
    count_min = math.floor(count/60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = "0" + str(count_sec)
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()

        

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodora")
window.config(padx= 100, pady= 50, bg=YELLOW)



canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font= (FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text ="Timer", fg=GREEN, bg=YELLOW, font= (FONT_NAME, 25, "bold"))
timer_label.grid(column=1, row=0)


start_button = Button(text="start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="reset", command=reset)
reset_button.grid(column=2, row=2)

checkmarks = Label(text="", fg=GREEN, bg=YELLOW, font= (FONT_NAME, 12, "bold"))
checkmarks.grid(column=1, row=3)


window.mainloop()