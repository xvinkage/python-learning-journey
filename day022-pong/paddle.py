from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x, y):

        super().__init__()
        self.goto(x, y)
        self.setheading(90)
        self.pu()
        self.color("white")
        self.shape("rectangle")

    def move_up(self):
        if self.ycor() >= 200:
            pass
        else:
            self.forward(20)
        
    def move_down(self):
        if self.ycor() <= -300:
            pass
        else:
            self.backward(20)
