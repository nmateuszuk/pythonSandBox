

from turtle import Turtle, Screen
import another_module
print(another_module.another_variable)

# import turtle
# timmy = turtle.Turtle()

timmy = Turtle()
timmy.shape("turtle")
timmy.color("coral")

timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
