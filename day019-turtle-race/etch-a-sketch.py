from turtle import Turtle, Screen

pen = Turtle()
screen = Screen()
screen.title("Etch-A-Sketch")


def move_forward():
    pen.forward(10)


def move_backward():
    pen.backward(10)


def move_right():
    pen.right(10)


def move_left():
    pen.left(10)


def clear():
    pen.pu()
    pen.clear()
    pen.home()
    pen.pd()


screen.listen()

screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=move_right, key="d")
screen.onkey(fun=move_left, key="a")
screen.onkey(fun=clear, key="c")


screen.exitonclick()


