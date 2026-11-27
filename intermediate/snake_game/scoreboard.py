"""board module"""

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("DejaVu Sans", 16, "normal")


class Scoreboard(Turtle):
    """scoreboard class"""

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", encoding="utf-8") as data:
            self.high_score = int(data.read())
        self.color("yellow")
        self.penup()
        self.goto(0, 250)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        """update scoreboard"""
        self.write(f"Score: {self.score}\nHightest: {self.high_score}", move=False,
                   align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """increase score"""
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def record(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w", encoding="utf-8") as data:
                data.write(f"{self.high_score}")

    def game_over(self):
        """collision"""
        self.goto(0, 0)
        self.color("red")
        self.write("Game Over!", move=False,
                   align=ALIGNMENT, font=FONT)
