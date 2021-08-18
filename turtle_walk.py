from turtle import Turtle, Screen
import random
import turtle as t

tim = Turtle()
t.colormode(255)


# tim.shape("turtle")
# tim.color("red")

# #Draw a square using Turtle
# for i in range(4):
#     tim.forward(100)
#     tim.right(90)

# #Draw a dash line
# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# #Draw Different shapes
#
# def draw_shape(number_sides, color):
#
#     for i in range(3, number_sides + 1):
#         inner_angle = 360/i
#         tim.color(colors[i - 3])
#         for number in range(i):
#             tim.forward(100)
#             tim.right(inner_angle)
#
# colors = ["DeepSkyBlue", "IndianRed", "green", "SeaGreen", "purple", "brown", "wheat", "maroon", "grey", "orange"]
#
#
# # draw = draw_shape(10 , colors)
#
# # Draw random walk
# def random_walk(color, angle):
#     for i in range(100):
#         tim.color(random.choice(color))
#         tim.pensize(8)
#         tim.speed("fastest")
#         walk_length = random.randint(15, 50)
#         tim.forward(walk_length)
#         turn_side = random.choice(angle)
#         tim.setheading(turn_side)

# Draw path using random colors
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def random_walk(angle):
    for i in range(100):
        tim.color(random_color())
        tim.pensize(8)
        tim.speed("fastest")
        walk_length = random.randint(15, 50)
        tim.forward(walk_length)
        turn_side = random.choice(angle)
        tim.setheading(turn_side)


turn_angle = [0, 90, 180, 270]
walk_free = random_walk(turn_angle)
screen = Screen()
screen.exitonclick()
