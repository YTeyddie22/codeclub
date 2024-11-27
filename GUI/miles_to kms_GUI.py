from tkinter import *

window = Tk()

window.title('Distance converter ')

window.minsize(height=400, width=500)
window.config(padx=30,pady=30)



def converter():
    miles =float(miles_input.get())
    km = round(miles * 1.609)
    km_result.config(text=f"{km}")
    


miles_input = Entry(width=10)
miles_input.grid(column=1,row=0)

mile_label = Label(text="Miles")
mile_label.grid(column=2,row=0)


is_equal_label = Label(text="Is equal to")
is_equal_label.grid(column=0,row=1)


km_result = Label(text="0")
km_result.grid(column=1,row=1)


km_label = Label(text="Kms")
km_label.grid(column=2,row=1)


calc_button = Button(text='Calculate', command=converter)
calc_button.grid(column=1,row=2)



#TkInter widgets
'''
Text
Button
Label
Scale
Spinbox
Entry
Checkbox
Radiobutton
Listbox

'''
window.mainloop()