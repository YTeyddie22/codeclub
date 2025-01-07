from tkinter import *
import math
import os

absolute_path = os.path.dirname(__file__)
img_name = "tomato.png"
image_path = os.path.join(absolute_path, img_name)

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    count_down(5 * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    
    count_min = math.floor(count / 60)
    count_sec = count % 60
    
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    if count > 0:
        canvas.itemconfig(timer_text, text = f"{count_min}: {count_sec}")
        window.after(1000, count_down, count - 1)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("POMODORO")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg = GREEN,bg = YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=image_path)
canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(100,130,text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start",  highlightthickness=0, command=start_timer)
start_button.grid(column=0, row = 2)

reset_button = Button(text="Reset",  highlightthickness=0)
reset_button.grid(column=2, row=2)

check_marks = Label(text="Fixed", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)






window.mainloop()