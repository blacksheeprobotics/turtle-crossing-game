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
sleep_factor = 0.1
while game_is_on:
    time.sleep(sleep_factor)
    screen.update()

    # add every sixth car generator:
    if car_gen_counter == 6:
        car_manager.create_car()
        car_gen_counter = 0
    else:
        car_manager.move_cars()

    # detect turtle-car collision:
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False

    # detect turtle moving to the other side:
    if player.passed_finish_line():
        sleep_factor /= 1.5

    car_gen_counter += 1

screen.exitonclick()
