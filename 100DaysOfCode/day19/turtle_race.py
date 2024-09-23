from turtle import Turtle, Screen

tim_the_turtle = Turtle()
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(
    "make your bet", "which turtle will win the race? Enter the color: ")

tim_the_turtle = Turtle()


screen.exitonclick()
