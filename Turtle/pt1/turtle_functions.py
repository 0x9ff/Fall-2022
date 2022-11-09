# turtle_functions.py
# created 10/17/2022

import turtle

# window config
window = turtle.Screen()
window.colormode(255)

mr = turtle.Turtle()
mr.speed(0)

def square(x, y, side, pensize=1, color="black"):
    # make ze turtle face right
    mr.setheading(0)

    mr.pensize(pensize)
    mr.pencolor(color)
    mr.penup()
    mr.goto(x, y)
    mr.pendown()

    mr.forward(side)
    mr.right(90)
    mr.forward(side)
    mr.right(90)
    mr.forward(side)
    mr.right(90)
    mr.forward(side)
    mr.right(90)

# use the square function
square(300, 300, 50)
square(-300, 300, 75)

# draw a square in the very center with length
square(-50, 50, 100)

# using optional parameters: write the variable_name = value
square(250, -300, 50, pensize=5)
square(100, 100, 25, color="green")
square(102, 102, 25, color=(0, 200, 50))

# window mainloop config - **Do Not Delete**
window.mainloop()