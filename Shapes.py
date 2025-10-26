import turtle

screen = turtle.Screen()
screen.bgcolor("black") 
screen.title("Polygons with Turtle")


t = turtle.Turtle()
t.speed(3)  

t.penup()
t.goto(-200, 100)  
t.pendown()
t.color("red", "red")  
t.begin_fill()
for _ in range(3):
    t.forward(100)
    t.left(120)
t.end_fill()

t.penup()
t.goto(50, 100)
t.pendown()
t.color("blue", "blue")
t.begin_fill()
for _ in range(2):
    t.forward(150) 
    t.left(90)
    t.forward(80)
    t.left(90)
t.end_fill()

t.penup()
t.goto(-50, -100)
t.pendown()
t.color("yellow", "yellow")
t.begin_fill()
for _ in range(6):
    t.forward(70)
    t.left(60)
t.end_fill()

turtle.done()