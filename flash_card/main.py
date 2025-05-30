import os
import pandas
import random
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

images_absolute_path = os.path.dirname(__file__)+"/images"
data_absolute_path = os.path.dirname(__file__)+"/data/french_words.csv"

# Images
front_card_image = images_absolute_path+"/card_front.png"
back_card_image = images_absolute_path+"/card_back.png"
correct_image = images_absolute_path+"/right.png"
wrong_image = images_absolute_path+"/wrong.png"


data = pandas.read_csv(data_absolute_path)
to_learn = data.to_dict(orient = "records")



def next_card():
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text = "French")
    canvas.itemconfig(card_word, text = current_card["French"])
    
    


window  = Tk()

window.title("Flash")
window.config(padx=50, pady=50,bg=BACKGROUND_COLOR)

# The overlay of the window object

canvas = Canvas(width=800, height=530)
front_card = PhotoImage(file=front_card_image)
canvas.create_image(400,260,image=front_card)
card_title = canvas.create_text(400,150,text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400,260,text="", font=("Ariel", 40, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0,column=0, columnspan=2)


cross_image = PhotoImage(file=wrong_image)
cross_button = Button(image=cross_image,highlightthickness=0,command=next_card)
cross_button.grid(row=1, column=0)

check_image = PhotoImage(file=correct_image)
check_button = Button(image=check_image,highlightthickness=0,command=next_card)
check_button.grid(row=1, column=1)

next_card()

window.mainloop()

