from turtle import Screen
from scoreboard import Scoreboard
from food import Food
from snake import Snake

import time

#Init the Screen
screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

#Create the snake object
snake = Snake()
food = Food()
scoreboard = Scoreboard()

#Listen to key binds
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
#Init the Game
game_is_on = True

#Checking is the game is continuing and moving snake body
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    #food collision
    if(snake.head.distance(food) < 15):
        food.refresh()
        snake.extend_segment()
        scoreboard.add_score()

    #Detect wall collision
    if(snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290):
        game_is_on = False
        scoreboard.game_over()
        
     #Detect collision with tail
    for segment in snake.segments:
        if(segment == snake.head):
            pass
        elif(snake.head.distance(segment) < 10):
           game_is_on = False
           scoreboard.game_over() 
     
screen.exitonclick()