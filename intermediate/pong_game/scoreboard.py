"""board module"""

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("DejaVu Sans", 24, "normal")


class Scoreboard(Turtle):
    """scoreboard class"""

    def __init__(self, username, position):
        super().__init__()
        self.name = username
        self.score = 0
        self.color("yellow")
        self.penup()
        self.goto(position)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        """update scoreboard"""
        self.write(f"{self.name}: {self.score}", move=False,
                   align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """increase score"""
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        """winner"""
        self.goto(0, 0)
        self.color("red")
        self.write(f"{self.name} win!", move=False,
                   align=ALIGNMENT, font=FONT)
