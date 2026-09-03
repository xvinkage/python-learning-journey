from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title = "Make your bet", prompt ="Pick a color. Which Turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple", ]
all_racers = []

for index, color in enumerate(colors):
    racer = Turtle(shape="turtle")
    racer.pu()
    racer.color(color)
    pos = index
    coord = pos * 30
    racer.goto(x=-235, y=-50 + coord)
    all_racers.append(racer)


if user_bet:
    is_race_on = True

while is_race_on:
    for racer in all_racers:
        if racer.xcor() > 230:
            is_race_on = False
            winning_color = racer.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is the winner")
            else:
                print(f"You Lost! The {winning_color} turtle is the winner")
        movement = random.randint(0, 10)
        racer.forward(movement)

screen.exitonclick()
