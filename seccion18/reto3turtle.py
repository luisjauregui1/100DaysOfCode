from turtle import Turtle, Screen
import random
tim = Turtle()
tim.shape('classic')
tim.pensize(5)
colors = ["medium blue","midnight blue", "dark green","maroon","blue violet","medium violet red","dark goldenrod","saddle brown","light slate gray"]

grados = 360
lados = 2

for i in range(8):
    lados = lados + 1
    grado = grados/ lados
    tim.color(random.choice(colors))
    for j in range(lados):
        tim.right(grado)
        tim.forward(100)
        
    

screen = Screen()
screen.exitonclick()

