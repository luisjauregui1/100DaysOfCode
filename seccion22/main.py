import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

jugador = Player()
car_manager = CarManager()
score_board = Scoreboard()

screen.listen()
screen.onkey(jugador.up, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    
    # Detect collision with the car
    for car in car_manager.all_cars:
        if car.distance(jugador) < 20:           
            score_board.game_over()
            game_is_on = False
        
    # Detect succesful crossing
    if jugador.ycor() > 270:
        # next level
        jugador.next_level()
        score_board.next_level()
        car_manager.level_up()
    

screen.exitonclick()