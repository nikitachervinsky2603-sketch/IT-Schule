import turtle

window = turtle.Screen()
window.bgcolor("black")

leonardo = turtle.Turtle()
leonardo.color("green")

def square():
    for a in range(4):
        leonardo.forward(100)
        leonardo.right(90)

def turtle():
    for i in range(32):
        square()
        leonardo.right(11.25)

turtle()