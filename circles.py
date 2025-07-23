from turtle import Turtle, Screen
import turtle as t
import random


def random_color():
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return color


tim = Turtle()
tim.speed("fastest")
tim.width(3)
t.colormode(255)

step = 15
for i in range(0, 360 + step, step):
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(i)

screen = Screen()
screen.exitonclick()
