from tkinter import *
import os

absolute_path = os.path.dirname(__file__)
img_name = "logo.png"
image_path = os.path.join(absolute_path, img_name)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password manager")
window.config(padx=20,pady=20)


canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file=image_path)
canvas.create_image(100,100, image=logo_img)



window.mainloop()