from turtle import Turtle
import random
colors = ["#4169E1","#00FF00","#98FB98","#000080","#000080","thistle","Crimson","LightCoral","DeepPink"]

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color(random.choice(colors))
        self.refresh()

    def refresh(self):
        self.x_cord = random.randint(-280, 280)
        self.y_cord = random.randint(-280, 280)
        self.goto(self.x_cord, self.y_cord)

    def random_colors(self):
        self.color(random.choice(colors))

    def game_over(self):
        self.goto(0, 0)
