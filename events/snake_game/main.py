from turtle import Screen
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



screen.exitonclick()