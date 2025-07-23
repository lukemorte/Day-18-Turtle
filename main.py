from turtle import Turtle, Screen
import turtle as t
import colorgram
import random

FILENAME = 'damien.png'
color_list = []


def get_random_color(p_color_list):
    return random.choice(p_color_list)


def create_color_library(size):
    colors = colorgram.extract(FILENAME, size)
    arr = [tuple(col.rgb) for col in colors if col.proportion < 0.1]
    arr = arr[2:]   # vymaže ještě pro jistotu první dva prvky pole, zřejmě také šedobílá
    return arr


def draw_circles(x_count, y_count, c_size, distance):
    for y in range(y_count):
        for x in range(x_count):
            tim.color(get_random_color(color_list))
            tim.dot(c_size)
            tim.forward(distance)
        tim.setx(0)
        tim.sety(tim.ycor() + distance)


tim = Turtle()
tim.shape('circle')
tim.speed('fastest')
tim.hideturtle()

t.colormode(255)
color_list = create_color_library(10)

tim.penup()
draw_circles(10, 10, 20, 50)

screen = Screen()
screen.exitonclick()
