from turtle import Screen
import time
from paddle import Paddle
from ball import Ball

game_is_on = True;

screen = Screen();
screen.tracer(0)
screen.bgcolor("black");
screen.setup(width=800, height=600)
screen.title("Pong")

right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))

ball = Ball()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")


while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    
    if(ball.ycor() > 280 or ball.ycor() < -280):
        ball.bounce()


screen.exitonclick()