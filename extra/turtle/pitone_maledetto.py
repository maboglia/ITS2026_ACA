from turtle import Turtle, done
from random import choice
from time import sleep

t = Turtle()
colors = ['red', 'green', 'blue', 'orange', 'purple', 'pink', 'violet','Indigo', 'Crimson','Teal']
t.color(choice(colors))

k = 50
k2 = k * 2
k3 = k * 3
k4 = k * 4

t.pensize(6)

def muovi(t: Turtle, pos_x, pos_y):
    print(f"Prima di muovere {t.xcor()} {t.ycor()}")  
    t.penup()
    t.goto(pos_x, pos_y)
    t.pendown()
    print(f"Dopo aver mosso {t.xcor()} {t.ycor()}")  

def drawLine(t, length, radius):
    print(f"Prima di disegnare {t.xcor()} {t.ycor()}")  
    t.left(angle=radius)
    t.forward(length)
    print(f"Dopo aver disegnato {t.xcor()} {t.ycor()}")  

def draw_O(t, x, y):
    t.circle(50)

def draw_T(t: Turtle, x, y):
    print(f"Scrivo T {x} {y}")
    drawLine(t, k2, 0)
    muovi(t, x - k, 100)
    print(f"Scrivo T {x} {y}")
    drawLine(t, k2, -90)
    muovi(t, x, y)
    print(f"Scrivo T {x} {y}")

def draw_P(t):
    print(f"Scrivo P {t.xcor()} {t.ycor()}")
    drawLine(t, 100, 90)
    drawLine(t, 50, -90)
    drawLine(t, 50, -90)
    drawLine(t, 50, -90)

def draw_I(t: Turtle):
    print(f"Scrivo I {t.xcor()} {t.ycor()}")
    drawLine(t, 100, 270)

def draw_N(t:Turtle):
    print(f"Scrivo N {t.xcor()} {t.ycor()}")
    drawLine(t, 100, 90)
    drawLine(t, 120, -145)
    drawLine(t, 100, 145)

def draw_E(t: Turtle):
    print(f"Scrivo N {t.xcor()} {t.ycor()}")
    drawLine(t, 100, 0)
    drawLine(t, 50, -90)
    muovi(t, t.xcor()-k, t.ycor()-k)
    drawLine(t, 50, 0)
    muovi(t, t.xcor()-k, t.ycor()-k)
    drawLine(t, 50, 0)

# t.goto(-200, 0) # Moves to new position

# t.left(angle=90)
# t.forward(100)

muovi(t, -300, 0)
draw_P(t)

muovi(t, -200, 0)
draw_I(t)

muovi(t, -100, 0)
draw_T(t, -100, 0)

muovi(t, 0, 0)
draw_O(t, 0, 0)

muovi(t, 100, 0)
draw_N(t)

muovi(t, 200, 0)
draw_E(t)

# ---------------------------

step = -470
for c in 'MALEDETTO':
    muovi(t, step, -200)
    t.color(choice(colors))
    t.write(c, font=("Tahoma", 100, "bold"))
    step = step + 100

t.penup()
t.home()
sleep(0.1)
t.clear()
sleep(0.1)
t.screen.bgcolor('black')
sleep(0.3)
t.screen.bgpic('./python.gif')

t.sety(-300)
t.pendown()
t.pensize(15)
t.color('red')
t.circle(300)

t.penup()
t.goto(x = -207, y = -207)
t.pendown()
t.left(45)
t.forward(590)

done()