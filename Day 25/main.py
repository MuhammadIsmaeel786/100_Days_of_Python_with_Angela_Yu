import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# how we can get x,y values from screen
# def get_mouse_click_cor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_cor)
# turtle.mainloop()
df = pd.read_csv("50_states.csv")
guessed_states = []
all_states = df.state.to_list()
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{guessed_states}/50 States correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")

        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = df[df.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
