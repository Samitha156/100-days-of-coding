from turtle import Turtle
import pandas

class GuessChecker:
    def __init__(self):
        self.data = pandas.read_csv("50_states.csv")
        self.state_list = self.data.state.to_list()
        self.missing_states = []

    def guess(self, user_guess):
        if user_guess in self.state_list:
            return True

    def coordinate(self, user_guess):
        state_data = self.data[self.data.state == user_guess]
        return state_data.x , state_data.y

    def states_to_learn(self, guessed_states):
        # for state in self.state_list:
        #     if state not in guessed_states:
        #         self.missing_states.append(state)
        self.mising_states = [state for state in self.state_list if state not in guessed_states]
        new_data = pandas.DataFrame(self.missing_states)
        new_data.to_csv("states_to_learn.csv")




