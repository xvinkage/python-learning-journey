from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My super unique snake game")
screen.tracer(0)


snake = Snake()
snake.create_body()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(fun=snake.move_up, key="Up")
screen.onkey(fun=snake.move_down, key="Down")
screen.onkey(fun=snake.move_right, key="Right")
screen.onkey(fun=snake.move_left, key="Left")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
#collision with food
    if snake.head.distance(food) < 15:
        snake.add_segment()
        scoreboard.update_score()
        food.refresh()
#collision with walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False 
        scoreboard.game_over()
#collision with tail
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

#collision with tail
screen.exitonclick()
