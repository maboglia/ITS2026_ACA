import turtle
from random import randint

turtle.speed(0)
turtle.bgcolor("black")
attempt = randint(0, 1)

if attempt == 0:
    turtle.color("#00FF00")
else:
    turtle.color("#00FFFF")
turtle.hideturtle()

for x in range(200):
    turtle.forward(x)
    turtle.left(x-1)
    

    
turtle.done()