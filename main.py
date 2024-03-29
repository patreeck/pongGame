from turtle import Screen
from padle import Paddle
from ball import Ball
from scoreBoard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG !")
screen.tracer(0)  # Turn off the animation
screen.listen()

paddle_right = Paddle(xcor=350, ycor=0)
paddle_left = Paddle(xcor=-350, ycor=0)
ball = Ball()
scoreBoard = ScoreBoard()

screen.onkey(paddle_right.up, "Up")
screen.onkey(paddle_right.down, "Down")
screen.onkey(paddle_left.up, "w")
screen.onkey(paddle_left.down, "s ")
paddle_left.create_paddle()
paddle_right.create_paddle()

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # detect collagen with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collagen with paddle
    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.speed("fastest")
        ball.bounce_x()
    # right misses
    if ball.xcor() > 380:
        scoreBoard.clear()
        scoreBoard.l_point()
        print("Left score :", scoreBoard.l_score)

        ball.reset_position()
        ball.bounce_x()
    # left misses
    if ball.xcor() < -380:
        scoreBoard.clear()
        scoreBoard.r_point()
        ball.reset_position()
        ball.bounce_x()

    if scoreBoard.l_score == 10:
        scoreBoard.game_over("LEFT PLAYER")
        game_on = False
    if scoreBoard.r_score == 10:
        scoreBoard.game_over("RIGHT PLAYER")
        game_on = False
screen.exitonclick()
