from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        self.cars = []
        self.move_speed = STARTING_MOVE_DISTANCE        
        

    def spawn_car(self):
        car = Turtle()
        car.pu()
        car.shape("square")
        car.shapesize(1, 2)
        car.color(random.choice(COLORS))
        y = random.randint(-250, 250)
        car.goto(300, y)
        self.cars.append(car)

    def move_forward(self):
        for car in self.cars:
            car.backward(self.move_speed)

    def level_up(self):
        self.move_speed += MOVE_INCREMENT