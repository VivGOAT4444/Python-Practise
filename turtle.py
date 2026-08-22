import turtle

screen = turtle.Screen()
screen.bgcolor("lightblue")

artist = turtle.Turtle()
artist.pensize(3)
artist.speed(5)


colors = ["red", "green", "blue", "yellow"]
for color in colors:
    artist.color(color)
    artist.forward(100)
    artist.right(90)


artist.hideturtle()


turtle.done()
