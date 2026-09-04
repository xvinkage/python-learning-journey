from turtle import Screen, Turtle, TK
import pandas as pd


screen = Screen()
screen.title("U.S. States Game")
img = "blank_states_img.gif"
screen.addshape(img)

t = Turtle()
t.shape(img)

data_file = pd.read_csv("50_States.csv")
df = pd.DataFrame(data_file) 

num_states = len(df["state"])
guessed_states = []


while len(guessed_states) < 50:
    num_correct = len(guessed_states)
    answer_state = screen.textinput(title=f"Guess the state {num_correct}/{num_states}", prompt="What's a state's name?").title()

    if answer_state == "Exit":
        states_to_learn = [states for states in df["state"].tolist() if states not in guessed_states]
        # states_to_learn = []

        # for states in df["state"].tolist():
        #     if states not in guessed_states:
        #         states_to_learn.append(states)
        data_frame = pd.DataFrame(states_to_learn, columns=["states"])
        data_frame.to_csv("states_to_learn.csv", index=False)
        break

    if answer_state in df["state"].tolist():
        found = df[df["state"] == answer_state]
        new_turtle = Turtle()
        state = found["state"].to_string(index=False)
        coords = found["x"].iloc[0], found["y"].iloc[0]
        new_turtle.hideturtle()
        new_turtle.pu()
        new_turtle.setpos(coords)
        new_turtle.write(state)

        if answer_state in guessed_states:
            TK.messagebox.showinfo("Notification", f"You already guessed {answer_state}")
        else:
            guessed_states.append(answer_state)
            TK.messagebox.showinfo("Notification", f"You guessed {answer_state} correctly")
    else:
        TK.messagebox.showwarning("Notification", "Incorrect Guess")



# def get_mouse_click_coords(x, y):
#     print(x, y)


# screen.onscreenclick(get_mouse_click_coords)
# screen.mainloop()

# screen.exitonclick()
