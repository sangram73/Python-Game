    from turtle import Turtle


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("black")
        
        
