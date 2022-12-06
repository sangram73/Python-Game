from turtle import Turtle
FONT=("Courier",20,"bold")

class Score(Turtle):
    def __init__(self,totalife) -> None:
        super().__init__()
        self.score=totalife
        self.penup()
        self.goto(-250,225)
        self.fillcolor("black")
        self.pendown()
        self.forward(500)
        self.left(90)
        self.forward(23)
        self.left(90)
        self.forward(500)
        self.left(90)
        self.forward(23)
        self.penup()
        self.setheading(0)
        self.goto(0,223)
        self.color("crimson")
        self.write(f"YOU HAVE {self.score} LIFE",align="center", font=FONT)
        self.hideturtle()
        
    def life_decrise(self):
        self.penup()
        self.score=self.score-1
        self.setheading(0)
        self.goto(0,223)
        self.color("crimson")
        self.clear()
        self.write(f"YOU HAVE {self.score} LIFE",align="center", font=FONT)
        self.pencolor("black")
        self.fillcolor("black")
        self.goto(-250,225)
        self.pendown()
        self.forward(500)
        self.left(90)
        self.forward(23)
        self.left(90)
        self.forward(500)
        self.left(90)
        self.forward(23)
    def game_over(self):
        self.pencolor("Deeppink")
        self.goto(0,0)
        self.write("you lose the game ",align="center",font=FONT)
    def win(self):
        self.penup()
        self.pencolor("Deeppink")
        self.goto(0,0)
        self.write("you won the game ", align="center",font=FONT)           
        