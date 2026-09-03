import colorgram
from turtle import Turtle, Screen, colormode
import random
# colors = colorgram.extract("img.jpg", 20)
# # print(colors)
# pic_colors = []
# final_color = []

# for first_color in colors:
#     red = first_color.rgb.r
#     green = first_color.rgb.g
#     blue = first_color.rgb.b
#     color = (red, green, blue)
#     final_color.append(color)

# print(final_color)

hirst_colorslist = [
    (236, 35, 108), (221, 231, 237), (145, 28, 66), 
    (230, 237, 232), (239, 74, 35), (7, 148, 95), 
    (222, 170, 44), (182, 158, 47), (44, 191, 232), 
    (28, 127, 194), (254, 223, 0), (125, 192, 77), 
    (85, 27, 91), (179, 40, 98), (243, 218, 57), 
    (43, 170, 114), (210, 132, 166), (208, 56, 33)]


t = Turtle()
screen = Screen()
colormode(255)
t.hideturtle()

for rows in range(10):
    t.pu()
    y = rows * 50
    t.setpos(-190, y - 210)
    t.pd()

    for new_line in range(10):
        t.pencolor(random.choice(hirst_colorslist))
        t.dot(20)
        t.pu()
        t.forward(50)

screen.exitonclick()
