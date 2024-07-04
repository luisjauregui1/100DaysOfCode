from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.forma = "square"
        self.color = 'white'
        self.tortugas = []
        self.crear_serpientes()
        self.head = self.tortugas[0]


    def crear_serpientes(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        nueva_tortuga = Turtle(shape=self.forma)
        nueva_tortuga.color(self.color)
        nueva_tortuga.penup()
        nueva_tortuga.goto(position)
        self.tortugas.append(nueva_tortuga)

    def extend(self):
        # add a new segment to the snake
        self.add_segment(self.tortugas[-1].position())
    
    def move(self):
        for seg_num in range(len(self.tortugas) - 1, 0, -1):
            new_y = self.tortugas[seg_num-1].ycor()
            new_x = self.tortugas[seg_num-1].xcor()
            self.tortugas[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
             
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
