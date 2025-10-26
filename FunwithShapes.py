import turtle

t = turtle.Turtle()
turtle.bgcolor("black")

t.color("red", "red")
t.begin_fill()
for i in range(3):
    t.forward(100)
    t.left(120)
t.end_fill()

t.penup()
t.forward(150)
t.pendown()

t.color("blue", "blue")
t.begin_fill()
for i in range(2):
    t.forward(150)
    t.left(90)
    t.forward(80)
    t.left(90)
t.end_fill()

t.penup()
t.forward(200)
t.pendown()

t.color("yellow", "yellow")
t.begin_fill()
for i in range(6):
    t.forward(70)
    t.left(60)
t.end_fill()

t.hideturtle()
turtle.done()