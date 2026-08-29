from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
scoreboard = ScoreBoard()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Toally unique pong game")
screen.register_shape("rectangle", ((0, 0), (0, 100), (20, 100), (20, 0)))

screen.tracer(0)
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

screen.listen()
screen.onkeypress(fun=l_paddle.move_up, key="w")
screen.onkeypress(fun=l_paddle.move_down, key="s")
screen.onkeypress(fun=r_paddle.move_up, key="Up")
screen.onkeypress(fun=r_paddle.move_down, key="Down")

ball = Ball()


game_is_on = True

while game_is_on:
    time.sleep(0.005)
    screen.update()
    ball.move()

    # wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # right paddle
    if ball.xcor() > 330 and ball.ycor() > r_paddle.ycor() and ball.ycor() < r_paddle.ycor() + 100 and ball.x_move > 0:
        ball.bounce_x()

    # left paddle
    if ball.xcor() < -330 and ball.ycor() > l_paddle.ycor() and ball.ycor() < l_paddle.ycor() + 100 and ball.x_move < 0:
        ball.bounce_x()

    # ball missed right
    if ball.xcor() > 390:
        scoreboard.l_point()
        ball.goto(0, 0)
        ball.bounce_x()

    # ball missed left
    if ball.xcor() < -390:
        scoreboard.r_point()
        ball.goto(0, 0)
        ball.bounce_x()