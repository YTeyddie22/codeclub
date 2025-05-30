import os

from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
images_absolute_path = os.path.dirname(__file__)+"/images"



front_card_image = images_absolute_path+"/card_front.png"
back_card_image = images_absolute_path+"/card_back.png"
correct_image = images_absolute_path+"/right.png"
wrong_image = images_absolute_path+"/wrong.png"


window  = Tk()

window.title("Flash")
window.config(padx=50, pady=50,bg=BACKGROUND_COLOR)

# The overlay of the window object

canvas = Canvas(width=800, height=530)
front_card = PhotoImage(file=front_card_image)
canvas.create_image(400,260,image=front_card)
canvas.create_text(400,150,text="Title", font=("Ariel", 40, "italic"))
canvas.create_text(400,260,text="Word", font=("Ariel", 40, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0,column=0, columnspan=2)


cross_image = PhotoImage(file=wrong_image)
cross_button = Button(image=cross_image,highlightthickness=0)
cross_button.grid(row=1, column=0)

check_image = PhotoImage(file=correct_image)
check_button = Button(image=check_image,highlightthickness=0)
check_button.grid(row=1, column=1)

window.mainloop()

