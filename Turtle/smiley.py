# smiley.py
# 3D (looking) square in a 2D turtle drawing
# created 10/25/2022

import turtle

window = turtle.Screen()
window.colormode(255)

smiley = turtle.Turtle()
window.tracer(0)


def square(x, y, side, pensize=1, color="black", fill_color="", angle=0):
    # make the turtle face the angle they specify
    smiley.setheading(angle)

    smiley.pensize(pensize)
    smiley.pencolor(color)
    smiley.penup()
    smiley.goto(x, y)
    smiley.pendown()

    # check if they chose a custom fill_color
    # fill_color would be something other than ""
    if fill_color != "":  # != means it is true if the two are different
        smiley.fillcolor(fill_color)
        smiley.begin_fill()

    smiley.forward(side)
    smiley.right(90)
    smiley.forward(side)
    smiley.right(90)
    smiley.forward(side)
    smiley.right(90)
    smiley.forward(side)
    smiley.right(90)

    if fill_color != "":
        smiley.end_fill()


def circle(x, y, radius, pensize=1, color="black", fill_color=""):
    # make the turtle face the angle they specify
    smiley.setheading(0)

    smiley.pensize(pensize)
    smiley.pencolor(color)
    smiley.penup()
    smiley.goto(x, y - radius)
    smiley.pendown()

    # check if they chose a custom fill_color
    # fill_color would be something other than ""
    if fill_color != "":  # != means it is true if the two are different
        smiley.fillcolor(fill_color)
        smiley.begin_fill()

    smiley.circle(radius)

    if fill_color != "":
        smiley.end_fill()


# all the code to draw the picture goes here
square(20, 50, 100, color="red", fill_color=(0, 150, 50))
circle(20, 50, 150, color="yellow", fill_color="yellow")

window.mainloop()