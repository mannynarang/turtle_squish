from turtle import Turtle


class Character(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.setpos(0, -280)
        self.right(270)
        self.shape("turtle")

    def move_forward(self):
        self.forward(20)


    def reset(self):
        self.setpos(0, -280)
