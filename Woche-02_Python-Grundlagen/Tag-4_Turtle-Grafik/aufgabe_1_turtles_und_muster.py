import turtle

window = turtle.Screen()
window.screensize(400, 400)

turtle.shape("turtle")
turtle.goto(-300, 300)

luigi = turtle.Turtle()
luigi.color("green")
luigi.shape("turtle")
luigi.goto(10, 10)

mario = turtle.Turtle()
mario.color("red")
mario.shape("turtle")
mario.goto(-10, -10)

ada = turtle.Turtle()
ada.color("blue")
ada.shape("turtle")
ada.goto(-20, 30)

for runden in range (20):

    turtle.pendown()
    turtle.forward(100)

    turtle.penup()
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)

    turtle.pendown()
    turtle.forward(100)

    turtle.penup()
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)