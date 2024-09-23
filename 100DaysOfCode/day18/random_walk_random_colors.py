# python tuple
# ordered, immutable (constant),

import turtle
import random
turtle.colormode(255)
my_tuple = (1, 3, 8)
print(my_tuple[0])

# to change put tuple to list

timmy_the_turtle = turtle.Turtle()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_col = (r, g, b)
    return random_col


directions = [0, 90, 180, 270]
timmy_the_turtle.pensize(15)
timmy_the_turtle.speed("fastest")

for _ in range(200):
    timmy_the_turtle.color(random_color())
    timmy_the_turtle.forward(30)
    timmy_the_turtle.setheading(random.choice(directions))
