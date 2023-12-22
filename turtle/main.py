import turtle as turtle
import random

turtle.colormode(255)
moon_turtle = turtle.Turtle();

directions = [0,90,180,270]


def random_color():
    r = random.randint(0,255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color
    

moon_turtle.width(15)
moon_turtle.speed("fast")
for _ in range(200):
    moon_turtle.forward(30);
    moon_turtle.setheading(random.choice(directions))
    moon_turtle.color(random_color())
     
     
"""
def drawShape(num_sides):
    for _ in range(num_sides):
        angle = 360 / num_sides
        moon_turtle.forward(100)
        moon_turtle.right(angle)

for num_shapes in range(3, 11):
    drawShape(num_shapes)
"""

screen = turtle.Screen()
screen.exitonclick()