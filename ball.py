from turtle import Turtle


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("black")
        self.x_pos = 10
        self.y_pos = 10

    def movo(self):
        new_x=self.xcor()-self.x_pos
        new_y=self.ycor()-self.y_pos
        
