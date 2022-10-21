import turtle

#########################
window = turtle.Screen()
window.colormode(255)

lol = turtle.Turtle()
window.tracer(0)
#########################

def square(x, y, side, pensize=1, color="blue"):
    lol.setheading(0)

    lol.pensize(pensize)
    lol.pencolor(color)
    lol.penup()
    lol.goto(x, y)
    lol.pendown()

#########################
window.mainloop()