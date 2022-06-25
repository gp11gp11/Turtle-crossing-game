from turtle import Screen
import time
from car  import Car
from player import Player
from scoreboard import Scoreboard
from random import choice

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")
screen.title("Pong")
screen.tracer(0)


car = Car()
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")



game_isnot_over = True
while game_isnot_over:
    screen.update()
    time.sleep(.1)
    

    car.make_car()
    car.move_car() 

    #Detect collision with car
    for vehicle in car.cars:
        if player.distance(vehicle) < 20:
            game_isnot_over = False
            scoreboard.game_over()

    #Detect whether turtle crossed by
    if player.ycor() > 350:
        scoreboard.winner()
        player.levelup()
        car.levelup_car()

    screen.update()

screen.exitonclick()