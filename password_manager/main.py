import os
from tkinter import *
from random import choice, randint, shuffle
from tkinter import messagebox
import pyperclip
import json


absolute_path = os.path.dirname(__file__)
img_name = "logo.png"
file_name = "data.json"
image_path = os.path.join(absolute_path, img_name)
data_path = os.path.join(absolute_path,file_name )

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    #Use List comprehension
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    
    # Use Entry module functions
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    #Create the new data
    
    new_data = {
        website: {
            "email": email,
            "password":password
        }
    }
    
     #Use the message box
    
    if len(website) == 0 or len(password) == 0  or len(email) == 0:
        messagebox.showinfo(title="Oh NOO!!!", message="Please fill in all the data")
    else:
        
        try:
            #Load, update the data into a json file
            with open(data_path, "r") as data_file:
                data = json.load(data_file)
                
        except FileNotFoundError:
            #Save the data into a json file
            with open(data_path, "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            
            with open(data_path, "w") as data_file:
                data.update(new_data)
                json.dump(data, data_file, indent=4)
        finally:    
            website_entry.delete(0,END)
            password_entry.delete(0,END)
                
        
# ---------------------------- Search Website PASSWORD ------------------------------- #

def search_password():
    website = website_entry.get()
    with open(data_path) as data_file:
        data = json.load(data_file)
        
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
    
    
   
    
    
    
    
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password manager")
window.config(padx=50,pady=50)


canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file=image_path)
canvas.create_image(100,100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1,column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2,column=0)
password_label = Label(text="Password:")
password_label.grid(row=3,column=0)


#Entries

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=3)
email_entry.insert(0, "teyddie63@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

#Buttons

generate_password_button = Button(text="Generate Password", width=15, command=generate_password)
generate_password_button.grid(row=3,column=2)
add_button = Button(text="Add", width=37, command=save)
add_button.grid(row=4,column=1, columnspan=2)
search_button = Button(text="Search", width=15,command=search_password)
search_button.grid(row=1,column=2)

window.mainloop()