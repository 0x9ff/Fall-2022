######################## ASSIGNMENT #############################
# Put your code for each part below the related comment         #
# 1. make the tower rotate through 3 colors all the way up      #
# 2. make a 2nd and 3rd tower to the right of the first that    #
#    also rotates through 4 and 5 colors respectively.          #
# 3. Make a 4th tower to the right of the others. However,      #
# this one is a pyramid of random colors.                       #
# Hint: in the loop, shorten the width and adjust the start     #
# location                                                      #
#                                                               #
# BONUS:                                                        #
# 1. Make the buildings have an outline (1 pixel of a different #
# color all the way around them).                               #
# 2. Make an Hourglass. (think pyramid, but with an inverse     #
# pyramid on top of it)  Give it an outline. Make it look like  #
# sand is dripping out of it and.                               #
#                                                               #
#               #########                                       #
#                #     #                                        #
#                 #...#                                         #
#                  #.#                                          #
#                   #                                           #
#                  #.#                                          #
#                 # . #                                         #
#                #.....#                                        #
#               #########                                       #
#                                                               #
#################################################################

# modulus_towers.py
# last modified 11/09/2022
# created 11/09/2022

import turtle as trtl

wn = trtl.Screen()
wn.colormode(255)

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(5)

#################################################################
# Dimensions of Tower & More
# Tower 1
x = -500
y = -150
width = 100
num_floors = 50

# Tower 2
#################################################################

# 1. Tower 1
for floor in range(num_floors):
    # set placement and color of turtle
    painter.penup()
    painter.goto(x, y)
    painter.color("gray")
    y = y + 5  # location of next floor

    if floor % 5 == 0:
        painter.color("red")
    elif floor % 5 == 1:
        painter.color("orange")
    elif floor % 5 == 2:
        painter.color("yellow")
    elif floor % 5 == 3:
        painter.color("green")
    else:
        painter.color("blue")



    # draw the floor
    painter.pendown()
    painter.forward(width)

# 2. Tower 2
for floor in range(num_floors):
    # set placement and color of turtle
    painter.penup()
    painter.goto(x, y)
    painter.color("gray")
    y = y + 5  # location of next floor

    if floor % 5 == 0:
        painter.color("red")
    elif floor % 5 == 1:
        painter.color("orange")
    elif floor % 5 == 2:
        painter.color("yellow")
    elif floor % 5 == 3:
        painter.color("green")
    else:
        painter.color("blue")



    # draw the floor
    painter.pendown()
    painter.forward(width)

# 3. Tower 3

# 4. Pyramid

# Bonus Hourglass

wn.mainloop()
