from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
SNAKE_FORWARD = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.fragments = []
        self.creating_snake()

    def creating_snake(self):
        for positions in STARTING_POSITIONS:
            self.add_segment(positions)

    def add_segment(self, positions):
        new_segmet = Turtle()
        new_segmet.penup()
        new_segmet.shape("square")
        new_segmet.color("white")
        new_segmet.goto(positions)
        self.fragments.append(new_segmet)

    def exted(self):
        self.add_segment(self.fragments[-1].position())

    def move(self):
        for frags in range(len(self.fragments) - 1, 0, -1):
            new_x = self.fragments[frags - 1].xcor()
            new_y = self.fragments[frags - 1].ycor()
            self.fragments[frags].goto(new_x, new_y)
        self.fragments[0].forward(SNAKE_FORWARD)

    def up(self):
        if self.fragments[0].heading() != DOWN:
            self.fragments[0].setheading(UP)

    def down(self):
        if self.fragments[0].heading() != UP:
            self.fragments[0].setheading(DOWN)

    def left(self):
        if self.fragments[0].heading() != RIGHT:
            self.fragments[0].setheading(LEFT)

    def right(self):
        if self.fragments[0].heading() != LEFT:
            self.fragments[0].setheading(RIGHT)
