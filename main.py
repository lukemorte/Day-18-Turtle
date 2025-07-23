from turtle import Turtle, Screen
import turtle as t
import colorgram

FILENAME = 'damien.png'
color_list = []


def create_color_library(size):
    colors = colorgram.extract(FILENAME, size)
    arr = [tuple(col.rgb) for col in colors if col.proportion < 0.1]
    arr = arr[2:]   # vymaže ještě pro jistotu první dva prvky pole, zřejmě také šedobílá
    return arr


tim = Turtle()
color_list = create_color_library(10)

print(color_list)


screen = Screen()
screen.exitonclick()
