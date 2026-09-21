"""board module"""

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("DejaVu Sans", 16, "normal")


class Scoreboard(Turtle):
    """scoreboard class"""

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("yellow")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        """update scoreboard"""
        self.write(f"Score: {self.score}", move=False,
                   align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """increase score"""
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        """collision"""
        self.goto(0, 0)
        self.color("red")
        self.write("Game Over!", move=False,
                   align=ALIGNMENT, font=FONT)
