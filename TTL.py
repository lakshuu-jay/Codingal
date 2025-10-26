import turtle

sc=turtle.Screen()
sc.bgcolor("Blue")
sc.setup(480,380)
sc.title("Welcome to Turtle Window")

board = turtle.Turtle()

for i in range(5):
    board.forward(100)
    board.left(90)