from turtle import Turtle, Screen
from car import Car
from score import Score
from character import Character
import random
import time

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=600, height=600)

score = Score()
character = Character()
score.display_score()
screen.onkey(character.move_forward, "Up")

screen.listen()
car_list = []
game_on = True
while game_on:
    screen.update()
    time.sleep(.10)
    if random.randint(0, 6) == 1:
        car_list.append(Car())

    for car in car_list:

        car.move_forward()

        if character.ycor() >= 280:
            score.update_score()
            score.display_score()
            character.reset()
        
        if car.distance(character) < 20:
            score.display_final()
            game_on=False


        if car.xcor() < -350:
            car.__del__()

    # if a collision with car/ game over

screen.exitonclick()
