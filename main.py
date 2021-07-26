from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    # wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

#    collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.boost()
        ball.bounce_x()
        print(ball.y_move, ball.x_move)



    if ball.xcor() > 400:
        scoreboard.l_point()
        scoreboard.update_scoreboard()
        ball.reset()
    elif ball.xcor() < -400:
        scoreboard.r_point()
        scoreboard.update_scoreboard()
        ball.reset()




screen.exitonclick()
