from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

is_race_on = True
user_bet = screen.textinput(
    title='Make Your Bet', prompt="Wich turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
informacion_tortugas = [('luh'), ('tim'), ('jon'), ('lol'), ('yun'), ('gin')]
figura = 'turtle'
ubicacio_Y = -100
index = 0
tortugas = []

for nombre in informacion_tortugas:
    nueva_tortuga = Turtle(shape=figura)
    nueva_tortuga.color(colors[index])
    nueva_tortuga.penup()
    nueva_tortuga.goto(x=-230, y=ubicacio_Y)
    ubicacio_Y += 40
    index += 1
    tortugas.append(nueva_tortuga)


# for turtle in tortugas:
#     print(f"Turtle color: {turtle.color()[0]}, Turtle position: {turtle.position()}")


while is_race_on:

    for torturga in tortugas:

        if torturga.xcor() > 230:
            is_race_on = False
            winning_color = torturga.color()
            break

        random_distance = random.randint(0, 10)
        torturga.forward(random_distance)


if winning_color[0] == user_bet:
    print(f"You've won! The {winning_color[0]} turtle is the winner!")
else:
    print(f"You've lost! The {winning_color[0]} turtle is winner!")


screen.exitonclick()
