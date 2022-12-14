from turtle import Turtle, Screen
import time
from box import Box
from padall import Paddle
from ball import Ball
from scorebord import Score


t = Turtle()
life =3
win = 0

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

score = Score(life)

paddle = Paddle()
screen.listen()
if paddle.xcor() < 230 or paddle.xcor() > -230:
    screen.onkey(paddle.Right, "Right")
    screen.onkey(paddle.Left, "Left")

ball = Ball()
FLAG = True
# for screen get update in every faction of sec
while FLAG:
    if life == 0:
        FLAG = False
        score.game_over()
        
        
    time.sleep(0.1)
    screen.update()
    ball.movo()

    if ball.xcor() > 230 or ball.xcor() < -230:
        ball.bounce_y()

    if ball.distance(paddle) < 50 and ball.ycor() > -220:
        ball.bounce_x()

    if ball.distance(box) < 50 and ball.ycor() > 150:
        box.venis()
        ball.bounce_y()
        win += 1

    if ball.distance(box2) < 50 and ball.ycor() > 150:
        box2.venis()
        ball.bounce_y()
        win += 1

    if ball.distance(box3) < 50 and ball.ycor() > 150:
        box3.venis()
        ball.bounce_y()
        win += 1

    if ball.distance(box4) < 50 and ball.ycor() > 150:
        box4.venis()
        ball.bounce_y()
        win += 1

    if ball.distance(box5) < 50 and ball.ycor() > 150:
        box5.venis()
        ball.bounce_y()
        win += 1

    if ball.distance(box6) < 50 and ball.ycor() > 150:
        box6.venis()
        ball.bounce_y()
        win += 1

    if ball.distance(box7) < 50 and ball.ycor() > 150:
        box7.venis()
        ball.bounce_y()
        win += 1

    if ball.distance(box8) < 50 and ball.ycor() > 150:
        box8.venis()
        ball.bounce_y()
        win += 1

    if ball.distance(box9) < 50 and ball.ycor() > 150:
        box9.venis()
        ball.bounce_y()
        win += 1

    if ball.distance(box10) < 50 and ball.ycor() > 150:
        box10.venis()
        ball.bounce_y()
        win += 1

    if ball.ycor() < -230:
        ball.reset()
        life -= 1
        score.life_decrise()

    if ball.ycor() > 200:
        ball.bounce_x()

    if win == 10:
        score.win()
        FLAG = False

screen.exitonclick()
