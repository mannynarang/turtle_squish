from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.setpos(-280, 280)
        self.hideturtle()
        self.color("white")

    def update_score(self):
        self.score += 1

    def display_score(self):
        self.clear()
        self.write(f"Level : {self.score}", move=False, align='left', font=('Arial', 12, 'normal'))

    def display_final(self):
        self.clear()
        self.write(f"Level : {self.score}", move=False, align='left', font=('Arial', 12, 'normal'))
        self.setpos(0, 0)
        self.write(f"Game over !! ", move=False, align='left', font=('Arial', 12, 'normal'))
