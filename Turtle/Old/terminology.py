# imports the turtle library
import turtle as trtl

# creates a screen object and assigns it to the wn variable
window = trtl.Screen()
window.colormode(255)

# creates a Turtle object and assigns it to the painter variable
painter = trtl.Turtle()
painter.speed(5)

painter.color("red")
painter.forward(100)
painter.left(120)
painter.fd(100)
painter.lt(120)
painter.forward(100)

painter.setheading(0)
painter.penup()
painter.goto(200, 300)
painter.pendown()
painter.color((0, 100, 255))
painter.pensize(10)
painter.fd(50)

# keeps the window open when we run the code (bottom of your code)

window.mainloop()