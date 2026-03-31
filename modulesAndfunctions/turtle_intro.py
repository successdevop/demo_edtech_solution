# import turtle
# turtle.pendown()
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.done()
import math
import turtle


def encircle_square(lenght: int) -> None:
    square(lenght)
    angle = math.radians(45)
    radius = lenght * math.cos(angle)
    turtle.right(135)
    turtle.circle(radius)


def square(length: int) -> None:
    for _ in range(4):
        turtle.forward(length)
        turtle.right(90)


# for _ in range(72):
#     square(120)
#     turtle.left(5)
encircle_square(300)
turtle.done()
