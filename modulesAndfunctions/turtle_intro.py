# import turtle
# turtle.pendown()
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.done()
# import math
import turtle
from math import radians, cos


def encircle_square(lenght: int) -> None:
    square(lenght)
    angle = radians(45)
    radius = lenght * cos(angle)
    turtle.right(135)
    turtle.circle(radius)


def square(length: int) -> None:
    for _ in range(4):
        turtle.forward(length)
        turtle.right(90)


turtle.speed("fast")
for _ in range(72):
    encircle_square(120)
    turtle.left(5)
# encircle_square(300)
turtle.done()
