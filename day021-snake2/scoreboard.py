from turtle import Turtle
ALIGNMENT = ('Courier', 20, 'normal')

class ScoreBoard(Turtle):

    def __init__(self,):
        self.score = 0

        super().__init__()
        self.hideturtle()
        self.goto(0, 250)
        self.color("Green")
        self.write(f"Score: {self.score}", move=False, align='center', font=ALIGNMENT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", move=False, align='center', font=ALIGNMENT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align='center', font=ALIGNMENT)
