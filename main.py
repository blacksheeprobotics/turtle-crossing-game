import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move_forward, "Up")

game_is_on = True
car_gen_counter = 1
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if car_gen_counter == 6:
        car_manager.create_car()
        car_gen_counter = 0
    else:
        car_manager.move_cars()

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False

    car_gen_counter += 1

screen.exitonclick()
