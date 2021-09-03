import turtle
import csv
import pandas
from guess_checker import GuessChecker
from state_locate import StateLocater

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

guess_checker = GuessChecker()
name_locator = StateLocater()

turtle.shape(image)
# Get the coordinate of where mouse click
# def get_mouse(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse)
# turtle.mainloop()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 are Correct",
                                    prompt="*********What's another state's name?*********").title()
    # print(answer_state)
    if answer_state == "Exit":
        guess_checker.states_to_learn(guessed_states)
        break
    if guess_checker.guess(answer_state):
        guessed_states.append(answer_state)
        move_x, move_y = guess_checker.coordinate(answer_state)
        name_locator.locate_name(int(move_x), int(move_y), answer_state)

# states_to_learn.csv()


# state_x = state_info["x"]
# state_y = state_info["y"]
# print(state_x)
# turtle.goto(state_x, state_y)
# int(state_y[1]))
# print(state_info)
# print(state_x)
# print(state_y)


# screen.exitonclick()
