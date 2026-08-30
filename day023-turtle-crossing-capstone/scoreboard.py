from turtle import Turtle

FONT = ("Courier", 24, "normal")
LEVEL = 1

class Scoreboard(Turtle):
    def __init__(self):
        self.level = LEVEL
        super().__init__()
        self.hideturtle()
        self.pu()
        self.goto(-200, 260)
        self.color("black")
        self.write(f"Level: {self.level}", align="Center", font=FONT)


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="Center", font=FONT)

    def increase_level(self):
        self.pu()
        self.goto(-200, 260)
        self.clear()
        self.level +=1
        self.write(f"Level: {self.level}", align="Center", font=FONT)
