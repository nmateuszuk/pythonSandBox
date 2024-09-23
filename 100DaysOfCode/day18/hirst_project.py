### This code will not work in repl.it as there is no access to the colorgram package here.###
## We talk about this in the video tutorials##
import colorgram
import turtle
import random

turtle.colormode(255)

rgb_colors = []
colors = colorgram.extract(
    '/workspaces/pythonSandBox/100DaysOfCode/day18/image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

rgb_colors = rgb_colors[5:]
print(rgb_colors)


timmy_the_turtle = turtle.Turtle()
timmy_the_turtle.speed("fastest")
timmy_the_turtle.penup()
timmy_the_turtle.hideturtle()
timmy_the_turtle.setheading(225)
timmy_the_turtle.forward(300)
timmy_the_turtle.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    timmy_the_turtle.dot(20, random.choice(rgb_colors))
    timmy_the_turtle.forward(50)
    if dot_count % 10 == 0:
        timmy_the_turtle.setheading(90)
        timmy_the_turtle.forward(50)
        timmy_the_turtle.setheading(180)
        timmy_the_turtle.forward(500)
        timmy_the_turtle.setheading(0)


screen = turtle.Screen()
screen.exitonclick()
