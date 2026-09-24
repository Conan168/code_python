"""Ball Module"""

from turtle import Turtle


class Ball(Turtle):
    """Ball class"""

    def __init__(self):
        super().__init__()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        self.create_ball()

    def create_ball(self):
        """create ball"""
        self.shape("circle")
        self.color("orange")
        self.penup()
        self.move()

    def move(self):
        x_position = self.xcor() + self.x_move
        y_position = self.ycor() + self.y_move
        self.goto(x=x_position, y=y_position)

    def bouncing_y(self):
        self.y_move *= -1

    def bouncing_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(x=0, y=0)
        self.move_speed = 0.1
        self.bouncing_x()
