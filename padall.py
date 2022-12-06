from turtle import Turtle


class Paddle(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.xposition = 0
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=4, stretch_wid=1)
        self.color("green")
        self.goto(0, -200)

    #   for paddle move to right
    def Right(self):
        x = self.xcor()+20
        self.goto(x, self.ycor())

    #   for paddle move to left
    def Left(self):
        x = self.xcor()-20
        self.goto(x, self.ycor())
