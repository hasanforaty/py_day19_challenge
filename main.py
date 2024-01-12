import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    """Move forward 10 space"""
    tim.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forward)


screen.exitonclick()
