import random
from turtle import Turtle
from random import Random


class Car(Turtle):

    def __init__(self):
        self.COLORS = ["white", "blue", "red", "green", "yellow"]
        super().__init__()
        self.color(random.choice(self.COLORS))
        self.shape("square")
        self.shapesize(1, 2)
        self.penup()
        self.set_position()


    def __del__(self):
        pass

    def move_forward(self):
        self.forward(-10)

    def set_position(self):
        y_cord = random.randrange(-280, 280,60)
        self.goto(280, y_cord)

