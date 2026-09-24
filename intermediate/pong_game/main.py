"""My pong game"""
from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

WINNER_SCORE = 10


def main():
    """main function"""

    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("My Pong Game")
    screen.tracer(0)

    right_paddle = Paddle((350, 0))
    left_paddle = Paddle((-350, 0))
    ball = Ball()
    right_scoreboard = Scoreboard("player2", (250, 220))
    left_scoreboard = Scoreboard("player1", (-250, 220))

    screen.listen()
    screen.onkey(right_paddle.up, "Up")
    screen.onkey(right_paddle.down, "Down")
    screen.onkey(left_paddle.up, "w")
    screen.onkey(left_paddle.down, "s")

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        ball.move()

        # detect collision with wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bouncing_y()

        # detect collision with right paddle
        if (
            ball.xcor() > 320
            and ball.distance(right_paddle) < 50
            or ball.xcor() < -320
            and ball.distance(left_paddle) < 50
        ):
            ball.bouncing_x()

        # detect miss of right paddle
        if ball.xcor() > 380:
            ball.reset_position()
            left_scoreboard.increase_score()

        # detect miss of left paddle
        if ball.xcor() < -380:
            ball.reset_position()
            right_scoreboard.increase_score()

        # detect winner
        if left_scoreboard.score >= WINNER_SCORE:
            game_is_on = False
            left_scoreboard.game_over()

        if right_scoreboard.score >= WINNER_SCORE:
            game_is_on = False
            right_scoreboard.game_over()

    screen.exitonclick()


if __name__ == '__main__':
    main()
