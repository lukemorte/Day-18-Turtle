from turtle import Turtle, Screen
import random


# vars


MOVE_LEN = 30
SPEED = 0
MAX_COUNT = 250
WIDTH = 15

directions = [0, 90, 180, 270]

color_list = [
    "darkseagreen",
    "darkseagreen1",
    "darkseagreen2",
    "darkseagreen3",
    "darkseagreen4",
    "darkslategray",
    "darkslategray1",
    "darkslategray2",
    "darkslategray3",
    "darkslategray4"
]


# def


def shuffle_color(color_list):
    tim.color(random.choice(color_list))


def set_rand_direction(p_directions):
    random_dir = random.choice(p_directions)
    tim.setheading(random_dir)


def draw_line(p_len):
    tim.forward(p_len)


# code

tim = Turtle()
tim.speed(SPEED)
tim.width(WIDTH)

for _ in range(MAX_COUNT):
    shuffle_color(color_list)
    set_rand_direction(directions)
    draw_line(MOVE_LEN)

screen = Screen()
screen.exitonclick()
