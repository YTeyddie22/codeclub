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
    
    #Collision with wall
    if(ball.ycor() > 280 or ball.ycor() < -280):
        ball.bounce_y()
    
    
    #Collision with paddle
    if(ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() > -320):
        print("ball collided")
        ball.bounce_x()
        
    #Detect ball passing right paddle
    if(ball.xcor() > 380):
        ball.reset_ball_position()
    
    #Detect ball passing left paddle
    if(ball.xcor() < -380):
        ball.reset_ball_position()
    


screen.exitonclick()