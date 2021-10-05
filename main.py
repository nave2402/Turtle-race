import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make Your bet", prompt="Which turtle will win the race? enter a color: ").lower()
colors = ["red", "blue", "green", "yellow", "orange", "purple"]
y_positions = [-140, -80, -20, 40, 100, 160]
turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    for color in colors:
        new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.speed(2)
    for position in y_positions:
        new_turtle.goto(x=-230, y=y_positions[turtle_index])
    turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You guessed right! the {user_bet} turtle win the race! :) ")
            else:
                print(f"You guessed wrong.. the {winning_color} turtle win the race! :( ")
        else:
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)







screen.listen()





screen.exitonclick()