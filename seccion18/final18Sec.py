import turtle as t
import random

jon = t.Turtle()
t.colormode(255)
jon.penup()
jon.speed('fastest')
jon.hideturtle()
screen = t.Screen()


color_list = [(228, 225, 221), (233, 206, 77), (226, 146, 86), (216, 228, 218), (231, 222, 225), (156, 15, 23), (118, 167, 188), (31, 109, 157), (213, 223, 229), (125, 175, 145), (232, 81, 47), (7, 97, 39), (174, 19, 15), (30, 129, 48), (203, 64, 25), (179, 184, 28), (12, 42, 76), (17, 62, 41), (234, 202, 12), (137, 83, 97), (90, 15, 25), (49, 166,76), (40, 28, 24), (176, 135, 147), (6, 66, 138), (47, 151, 195), (212, 70, 75), (231, 169, 160), (77, 134, 185), (168, 206, 177),(228, 225, 221), (233, 206, 77), (226, 146, 86), (216, 228, 218), (231, 222, 225), (156, 15, 23), (118, 167, 188), (31, 109, 157), (213, 223, 229), (125, 175, 145), (232, 81, 47), (7, 97, 39), (174, 19, 15), (30, 129, 48), (203, 64, 25), (179, 184, 28), (12, 42, 76), (17, 62, 41), (234, 202, 12), (137, 83, 97), (90, 15, 25), (49, 166,76), (40, 28, 24), (176, 135, 147), (6, 66, 138), (47, 151, 195), (212, 70, 75), (231, 169, 160), (77, 134, 185), (168, 206, 177)]


def random_color(lista):
    color = random.choice(lista)
    return color

    
aux = -230
for i in range(10):
    aux +=50
    jon.goto(-160,aux)
    for j in range(10):
        jon.dot(20, random_color(color_list))
        jon.forward(50)
        


screen.exitonclick()

# Mi version 👆
# Angela Version 👇

# import turtle as turtle_module
# import random

# turtle_module.colormode(255)
# tim = turtle_module.Turtle()
# tim.speed("fastest")
# tim.penup()
# tim.hideturtle()
# color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
# tim.setheading(225)
# tim.forward(300)
# tim.setheading(0)
# number_of_dots = 100

# for dot_count in range(1, number_of_dots + 1):
#     tim.dot(20, random.choice(color_list))
#     tim.forward(50)

#     if dot_count % 10 == 0:
#         tim.setheading(90)
#         tim.forward(50)
#         tim.setheading(180)
#         tim.forward(500)
#         tim.setheading(0)


# screen = turtle_module.Screen()
# screen.exitonclick()
