import random
from turtle import Turtle

COLORS = ["orange", "yellow", "blue", "Chartreuse", "purple", "crimson"]


class Box(Turtle):
    def __init__(self, position) -> None:
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=4, stretch_wid=2)
        self.penup()
        self.color(random.choice(COLORS))
        self.goto(position)

# for every hit the venis will be applyed
    def venis(self):
        self.reset()
        self.hideturtle()
