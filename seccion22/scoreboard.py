from turtle import Turtle
FONT = ("Courier", 18, "normal")
TEXT = "LEVEL:"

class Scoreboard(Turtle):
    
    
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.update_scoreboard()
        
        
    def update_scoreboard(self):
        self.penup()
        self.hideturtle()
        self.clear()
        self.goto(-240, 265)
        self.write(f'level: {self.score}', align='center', font=FONT)
        
        
    def next_level(self):
        self.score += 1
        self.update_scoreboard()
        
    
    def game_over(self):
        self.goto(0,0)
        self.write(f'GAME OVER', align='center', font=FONT)