from turtle import Turtle, Screen


# functions
def moving_forward():
    timmy.forward(10)


def moving_backward():
    timmy.backward(10)


def rotate_clockwise():
    timmy.setheading(timmy.heading() - 10)


def rotate_counter_clockwise():
    timmy.setheading(timmy.heading() + 10)


def clear_draw():
    timmy.penup()
    timmy.home()
    timmy.clear()
    timmy.pendown()


# Setups
timmy = Turtle()
screen = Screen()

screen.listen()
screen.onkey(key="w", fun=moving_forward)
screen.onkey(key="s", fun=moving_backward)
screen.onkey(key="a", fun=rotate_counter_clockwise)
screen.onkey(key="d", fun=rotate_clockwise)
screen.onkey(key="c", fun=clear_draw)
screen.exitonclick()
