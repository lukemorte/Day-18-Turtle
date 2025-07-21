from turtle import Turtle, Screen
from random import random

# vars


LINE_LEN = 100
MAX_SIDES = 10
SPEED = 4


# def


def draw_line():
    tim.forward(LINE_LEN)


def turn(p_side):
    div = 360 / p_side
    tim.right(div)


def draw_shape(sides):
    for n in range(sides):
        draw_line()
        turn(sides)


def shuffle_color():
    rnd = [random(), random(), random()]
    tim.color(rnd)

# code


tim = Turtle()
tim.speed(SPEED)
tim.width(2)


for sides in range(3, 11):
    shuffle_color()
    draw_shape(sides)



screen = Screen()
screen.exitonclick()
