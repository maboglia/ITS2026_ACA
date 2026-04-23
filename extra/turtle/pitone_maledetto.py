from turtle import Turtle, done
from random import choice

t = Turtle()
colors = ['red', 'green', 'blue', 'orange', 'purple', 'pink', 'violet']


def muovi(tartaruga: Turtle, pos_x, pos_y):
    tartaruga.penup()
    tartaruga.goto(pos_x, pos_y)
    tartaruga.pendown()

def drawLine(tartaruga, length, radius):
    tartaruga.color(choice(colors))
    tartaruga.left(angle=radius)
    tartaruga.forward(length)

# t.goto(-200, 0) # Moves to new position

# t.left(angle=90)
# t.forward(100)

muovi(t, -200, 0)
drawLine(t, 100, 90)


# t.right(90)
# t.forward(50)
drawLine(t, 50, -90)


# t.right(90)
# t.forward(50)
drawLine(t, 50, -90)

# t.right(90)
# t.forward(50)
drawLine(t, 50, -90)

# t.hideturtle()


muovi(t, -100, 0)
drawLine(t, 100, 270)

muovi(t, 0, 0)
drawLine(t, 100, 0)

muovi(t, 100, 0)
drawLine(t, 100, 0)


muovi(t, 200, 0)
drawLine(t, 100, 0)


muovi(t, 300, 0)
drawLine(t, 100, 0)




done()