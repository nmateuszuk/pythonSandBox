from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False
user_bet = screen.textinput(
    "make your bet", "which turtle will win the race? Enter the color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# tim_the_turtle_1 = Turtle(shape="turtle")
# tim_the_turtle_1.penup()
# tim_the_turtle_1.goto(x=-230, y=-100)

turtle_gang = {}

for i in range(1, 7):
    turtle_name = f"tim_the_turtle_{i}"
    turtle_gang[turtle_name] = Turtle(shape="turtle")
    turtle_gang[turtle_name].penup()
    turtle_gang[turtle_name].color(colors[i-1])
    turtle_gang[turtle_name].goto(x=-230, y=(-60 + i*30))

if user_bet:
    is_race_on = True

winning_color = ""
while is_race_on:
    for turtle in turtle_gang:
        if turtle_gang[turtle].xcor() > 230:
            is_race_on = False
            winning_color = turtle
        random_distance = random.randint(0, 10)
        turtle_gang[turtle].forward(random_distance)

print(f"the winner is {winning_color} his color is {
      turtle_gang[winning_color].pencolor()}")
if user_bet == turtle_gang[winning_color].pencolor():
    print("you win the bet")
else:
    print("you have lost the bet!")

screen.exitonclick()
