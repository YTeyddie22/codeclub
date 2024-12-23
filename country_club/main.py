import turtle 
import pandas as pd


guessed_states = []
screen = turtle.Screen()
screen.title("U.S States")

image = "blank_states_img.gif"
data = pd.read_csv("50_states.csv")
all_states = data['state'].to_list()

screen.addshape(image)
turtle.shape(image)


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What is another state's name?").title()

    if answer_state == "Exit":
        missing_state = [state for state in all_states  if state not in guessed_states]
        new_data = pd.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break
    
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data['state'] == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
    