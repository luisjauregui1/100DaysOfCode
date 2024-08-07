from turtle import Turtle

ALINGMENT = "center"
FONT = ("Courier", 14, "normal")
PATH = ('C:/Users/Gustavo/Documents/Programacion/100DaysOfCode/seccion20/data.txt')

class Score_board(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open(PATH) as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score:{self.score} High Score: {
                   self.high_score}', align=ALINGMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(PATH, mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
