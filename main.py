import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun=r_paddle.move_up, key="Up")
screen.onkeypress(fun=r_paddle.move_down, key="Down")

screen.onkeypress(fun=l_paddle.move_up, key="q")
screen.onkeypress(fun=l_paddle.move_down, key="a")

def game():
    game_is_on = True

    while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        # Detect collision with the top & bottom walls
        if ball.ycor() >= 280 or ball.ycor() <= -280:
            ball.bounce_y()

        # Detect collision with left and right walls
        if ball.xcor() > 380:
            ball.refresh()
            scoreboard.increase_score(l_score=1)

        if ball.xcor() < -380:
            ball.refresh()
            scoreboard.increase_score(r_score=1)

        # Detect collision with the paddle
        if (ball.xcor() > 320 and ball.distance(r_paddle) < 50) or (ball.xcor() < -320 and ball.distance(l_paddle) < 50):
            ball.bounce_x()
while True:
    game()

screen.exitonclick()