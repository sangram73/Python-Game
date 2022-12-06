from turtle import Turtle, Screen
import time
from box import Box
from padall import Paddle

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
t.hideturtle()
screen.setup(500, 500)
screen.title("Bubble shooter game")
# it will turn off the animation
screen.tracer(0)

box = Box(position1)
box2 = Box(position2)
box3 = Box(position3)
box4 = Box(position4)
box5 = Box(position5)
box6 = Box(position6)
box7 = Box(position7)
box8 = Box(position8)
box9 = Box(position9)
box10 = Box(position10)

paddle = Paddle()


flag = True
# for screen get update in every faction of sec
while flag:
    time.sleep(0.1)
    screen.update()


screen.exitonclick()
