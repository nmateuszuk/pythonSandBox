from turtle import Turtle, Screen

tim_the_turtle = Turtle()
screen = Screen()


def move_forwards():
    tim_the_turtle.forward(10)


def move_backwards():
    tim_the_turtle.backward(10)


def move_left():
    tim_the_turtle.left(10)


def move_right():
    tim_the_turtle.right(10)


def clear():
    tim_the_turtle.clear()
    tim_the_turtle.penup()
    tim_the_turtle.home()
    tim_the_turtle.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear)


screen.exitonclick()
