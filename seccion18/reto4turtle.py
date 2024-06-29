import turtle as t
import random

grados = [0,90,180,270]

jim = t.Turtle()
t.colormode(255)
jim.pensize(15)
jim.speed('fastest')


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    
    return (r,g,b)


for i in range(600):
    jim.color(random_color())
    jim.forward(30)
    jim.setheading(random.choice(grados))
    

pantalla = t.Screen()
pantalla.exitonclick()
