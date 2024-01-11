import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)


def get_mouse_click_coor(x, y):
    print(x, y)


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

is_game_over = False
correct_guesses = []

while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in correct_guesses]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        correct_guesses.append(answer_state)
        new_turtle = turtle.Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        state_data = data[data.state == answer_state]
        new_turtle.goto(int(state_data.x), int(state_data.y))
        new_turtle.write(state_data.state.item())
