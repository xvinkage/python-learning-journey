from turtle import Turtle
ALIGNMENT = ('Courier', 20, 'normal')

class ScoreBoard(Turtle):

    def __init__(self):
        self.score = 0
        self.high_score = 0

        super().__init__()
        self.hideturtle()
        self.goto(0, 240)
        self.color("Green")

        with open("./day020-021-024-snake/data.txt", mode="r") as file:
            self.high_score = int(file.read())

        self.update_display()

    def update_display(self):
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            move=False,
            align='center',
            font=ALIGNMENT
        )

    def update_score(self):
        self.score += 1
        self.update_display()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

        self.score = 0
        self.update_display()

        with open("./day020-021-024-snake/data.txt", mode="w") as file:
            file.write(f"{self.high_score}\n")

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", move=False, align='center', font=ALIGNMENT)
