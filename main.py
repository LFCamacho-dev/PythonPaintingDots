# import colorgram
import random
import turtle as turtle_module
from turtle import Turtle, Screen

# colors = colorgram.extract("images/image.jpg", 30)
# # rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

turtle_module.colormode(255)
lucho = Turtle()

color_list = [(58, 106, 148), (224, 200, 110), (134, 84, 58), (223, 138, 62),
              (196, 145, 171), (142, 178, 203), (139, 82, 105), (208, 90, 69),
              (237, 225, 233), (188, 80, 120), (69, 105, 90), (133, 182, 135),
              (133, 133, 74), (64, 156, 92), (47, 156, 193), (183, 192, 201),
              (213, 177, 191), (19, 58, 92), (20, 68, 113), (113, 123, 149),
              (227, 174, 166), (172, 203, 183), (156, 206, 217), (69, 58, 47),
              (72, 64, 53), (111, 46, 59), (53, 70, 64)]

# 10 x 10 wide, 20 size, 50 space between


def get_ready():
    lucho.speed(0)
    lucho.setheading(225)
    lucho.penup()
    lucho.forward(250)
    lucho.setheading(0)


def line_of_dots():
    for _ in range(10):
        lucho.dot(20, random.choice(color_list))

        lucho.forward(50)


def return_line():
    lucho.left(90)
    lucho.forward(50)
    lucho.left(90)
    lucho.forward(500)
    lucho.left(180)


def start_painting():
    get_ready()
    for a in range(10):
        line_of_dots()
        return_line()


start_painting()
screen = Screen()
screen.screensize(150, 150)
screen.exitonclick()
