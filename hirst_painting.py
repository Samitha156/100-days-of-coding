import colorgram
import turtle as turtle_module
import random

# colors = colorgram.extract('Hirstspotpainting.jpg', 30)
# all_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#
#     all_colors.append(new_color)
#     # print(colors[i].rgb)
# print(all_colors)

color_list = [(144, 76, 50), (188, 165, 117), (166, 153, 36), (14, 46, 85), (139, 185, 176),
              (146, 56, 81), (42, 110, 136), (59, 120, 99), (145, 170, 177), (87, 35, 30), (64, 152, 169),
              (220, 209, 93), (110, 37, 31), (100, 145, 111), (165, 99, 131), (91, 122, 172), (158, 138, 158),
              (177, 104, 82), (55, 52, 85), (206, 182, 195), (68, 48, 63), (73, 51, 71), (173, 201, 194),
              (175, 198, 201), (213, 182, 176), (37, 47, 45)]
turtle_module.colormode(255)
tom = turtle_module.Turtle()
tom.penup()
tom.setheading(225)
tom.forward(300)
tom.setheading(0)
tom.hideturtle()
tom.speed("fastest")
for rows in range(10):
    print(rows)
    for i in range(10):
        tom.dot(15, random.choice(color_list))
        tom.penup()
        tom.forward(50)
    if rows % 2 == 0:
        tom.setheading(90)
        tom.forward(50)
        tom.left(90)
        tom.forward(50)
    else:
        tom.setheading(90)
        tom.forward(50)
        tom.right(90)
        tom.forward(50)


screen = turtle_module.Screen()
screen.exitonclick()