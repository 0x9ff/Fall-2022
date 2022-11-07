#   This code draws a flower.
import turtle as trtl

window = trtl.Screen()
window.colormode(255)

painter = trtl.Turtle()
painter.speed(0)


# stem
painter.color("green")
painter.pensize(15)
painter.goto(0, -150)
painter.setheading(90)
painter.forward(100)


#  leaf
painter.setheading(270)
painter.circle(20, 120, 20)
painter.setheading(90)
painter.goto(0, -60)


# rest of stem
painter.forward(60)
painter.setheading(0)


# change pen
painter.penup()
painter.shape("circle")
painter.turtlesize(2)


# draw flower
painter.color("pink")
painter.goto(20,180)
petals = 0
for petals in range(18):
  painter.right(20)
  painter.forward(30)
  painter.stamp()


# ring 2 of flower
painter.goto(20,150)
painter.color("yellow")
petals = 0
for petals in range(12):
  painter.right(30)
  painter.forward(30)
  painter.stamp()


# ring 3 of flower
painter.goto(20,120)
painter.color("yellow")
petals = 0
for petals in range(9):
  painter.right(40)
  painter.forward(20)
  painter.stamp()


window.mainloop()