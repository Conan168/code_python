"""paddle module"""

from turtle import Turtle

PADDLE_WIDTH_STRETCH = 8


class Paddle(Turtle):
    """paddle"""

    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position):
        """new paddle"""
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=PADDLE_WIDTH_STRETCH)
        self.color("white")
        self.penup()
        self.goto(position)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
