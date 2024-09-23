from turtle import Turtle, Screen

tim_the_turtle = Turtle()
screen = Screen()


def move_forwards():
    tim_the_turtle.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()
