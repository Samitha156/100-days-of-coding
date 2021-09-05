from turtle import Turtle

class StateLocater:
    def __init__(self):
        self.all_names = []
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.turtle.penup()

    def locate_name(self,move_x,move_y, state_name):
        self.turtle.goto(move_x, move_y)
        self.turtle.write(state_name)

