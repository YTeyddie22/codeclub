from turtle import Screen, Turtle

game_is_on = True;
screen = Screen();
paddle = Turtle()


screen.tracer(0)
screen.bgcolor("black");
screen.setup(width=800, height=600)
screen.title("Pong")

paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350, 0)

while game_is_on:
    screen.update()

def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)
    
def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

screen.exitonclick()