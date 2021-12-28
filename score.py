import random
from turtle import Turtle
colors = ["#4169E1","#00FF00","#98FB98","#000080","#000080","thistle","Crimson","LightCoral","DeepPink"]


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color(random.choice(colors))
        self.penup()
        self.goto(-30, 250)
        self.hideturtle()
        self.angarishi()
        self.random_score_colors()

    def random_score_colors(self):
        self.color(random.choice(colors))

    def ganaxleba(self):
        self.write(f"ქულა : {self.score}", align='center', font=("Arial", 24, "normal"))


    def angarishi(self):
        self.clear()
        self.ganaxleba()
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("თამაში დასრულდა ! ", align='center', font=("Arial", 24, "normal"))
