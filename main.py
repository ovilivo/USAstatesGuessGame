import turtle
import pandas
screen = turtle.Screen()
screen.title("The U.S States")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
guessed_states = []
while len(guessed_states) < 50:
    answer_state = turtle.textinput(title=f"{len(guessed_states)}/50 States Guessed",
                                    prompt="Guess the State name").title()
    if answer_state == "Exit":
        remaining_states = []
        for state in state_list:
            if state not in guessed_states:
                remaining_states.append(state)
        learnData = pandas.DataFrame(remaining_states)
        learnData.to_csv("Remaining_States.csv")
        break
    if answer_state in state_list:
        guessed_states.append(answer_state)
        answer = turtle.Turtle()
        answer.hideturtle()
        answer.penup()
        state_data = data[data.state == answer_state]
        answer.goto(int(state_data.x), int(state_data.y))
        answer.write(answer_state)

remaining_states = []
for state in state_list:
    if state not in guessed_states:
        remaining_states.append(state)

pandas.to_csv()
screen.exitonclick()
