from turtle import Turtle, Screen
import random


def race():
    turtle_list = []
    colors = ['red', 'green', 'blue', 'purple', 'orange', 'yellow']
    # setUp
    screen = Screen()
    screen.setup(width=600, height=600)
    is_race_on = False
    user_bet = screen.textinput(title="Turtle Race", prompt="Which turtle will win the race? Enter a Color: ")
    per = 550 / len(colors)
    # Logics
    for color in colors:
        tim = Turtle()
        tim.color(color)
        tim.penup()
        tim.shape("turtle")
        y = -250 + (per * len(turtle_list))
        speed = random.randint(0, 10)
        tim.goto(x=-250, y=y)
        tim.speed(speed=speed)
        turtle_list.append(tim)
    if user_bet:
        is_race_on = True
    while is_race_on:
        for selected_turtle in turtle_list:
            selected_turtle.forward(random.randint(0, 10))
            if selected_turtle.xcor() > 300:
                winning_color = selected_turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You've won! The {winning_color} turtle is the winner !")
                else:
                    print(f"You've lost! The {winning_color} turtle is the winner !")
                return


race()
