import os
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

work_dir = os.getcwd() + "/Python/codeclub/events/snake_game/data.txt"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()     
        self.score = 0
        with open(work_dir) as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_score()
        self.hideturtle()
       
    
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} : High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        
    def add_score(self):
        self.score += 1
        self.update_score() 
        
    def reset(self):
        if(self.score > self.high_score):
            self.high_score = self.score
            with open(work_dir, mode = "w") as data:
               data.write(f"{self.high_score}") 
        self.score = 0
        self.update_score()
        
    #def game_over(self):
     #   self.goto(0, 0)
      #  self.write("Game Over!", align=ALIGNMENT, font=FONT)