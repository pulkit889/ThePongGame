from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(x=-100, y=200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(x=100, y=200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
