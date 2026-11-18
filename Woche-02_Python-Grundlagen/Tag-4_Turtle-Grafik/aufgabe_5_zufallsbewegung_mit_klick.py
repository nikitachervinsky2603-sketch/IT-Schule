
import turtle
import random

window = turtle.Screen()
window.bgcolor("black")
window.bgpic("681178_cbab4.gif")

leo = turtle.Turtle()
leo.shape("turtle")
leo.color("green")

def bewegung():
    leo.forward(random.randint(10, 50))
    leo.right(random.randint(-180, 180))
    leo.color(random.choice(["red", "green", "blue", "yellow"]))

    window.ontimer(bewegung, 500)

def click(x, y):
    leo.color(random.choice(["red", "green", "blue", "yellow"]))

leo.onclick(click)

bewegung()

turtle.done()
