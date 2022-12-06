from turtle import Turtle, Screen
import time
from box import Box

t = Turtle()

# position for box are placed
position1 = (180, 200)
position2 = (90, 200)
position3 = (0, 200)
position4 = (-90, 200)
position5 = (-180, 200)
position6 = (180, 140)
position7 = (90, 140)
position8 = (0, 140)
position9 = (-90, 140)
position10 = (-180, 140)

screen = Screen()
screen.setup(500, 500)
screen.title("Bubble shooter game")
# it will turn off the animation
screen.tracer(0)

box =Box(position1)
box =Box(position2)
box =Box(position3)
box =Box(position4)
box =Box(position5)
box =Box(position6)
box =Box(position7)
box =Box(position8)
box =Box(position9)
box =Box(position10)







screen.exitonclick()
