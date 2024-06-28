import turtle as t
import random

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    
    return (r,g,b)

tom = t.Turtle()
t.colormode(255)
tom.speed('fastest')

for i in range(45):
    tom.color(random_color())
    tom.setposition((0,0))
    tom.circle(100)
    tom.right(8)


screen = t.Screen()
screen.exitonclick()