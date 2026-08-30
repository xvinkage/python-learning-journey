import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
carmanager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun=player.move_forward, key="Up")
screen.onkeypress(fun=player.move_backward, key="Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carmanager.move_forward()
#chance of spawning a car
    if random.randint(1, 6) == 1:
        carmanager.spawn_car()
#collison with cars
    for car in carmanager.cars:
        if car.distance(player) < 10:
            game_is_on = False
            scoreboard.game_over()
#if pass the stage starts back at the beginning and increase lvel
    if player.ycor() > 280:
        player.starting_pos()
        scoreboard.increase_level()
        carmanager.level_up()

screen.exitonclick()