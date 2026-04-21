import turtle

t = turtle.Turtle()

t.goto(-200, 0) # Moves to new position

t.color("red")

t.left(angle=90)
t.forward(100)

t.right(90)
t.forward(50)

t.right(90)
t.forward(50)

t.right(90)
t.forward(50)

t.hideturtle()

t.left(90)
t.forward(50)

t.penup()       # Lifts the pen to avoid drawing
t.goto(-100, 0) # Moves to new position
t.left(90)
#t.forward(100)

t.pendown() 
t.left(angle=90)
t.forward(100)

t.penup()       # Lifts the pen to avoid drawing
t.goto(0, 0) # Moves to new position
# t.left(90)
# t.forward(100)

t.pendown() 
t.left(angle=90)
t.forward(100)





turtle.done()