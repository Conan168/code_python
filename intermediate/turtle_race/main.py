"""Game: Turtle racing """

from turtle import Turtle, Screen
import random


def main():
    """main"""

    screen = Screen()
    screen.setup(width=500, height=400)
    is_race_on = False
    user_bet = screen.textinput(
        title="Make your bet",
        prompt="Which turtle will win the race? red/orange/yello/green/blue/purple"
    ).lower()
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    y_position_of_first_turtle = 75
    all_turtles = []

    for index in range(6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[index])
        new_turtle.penup()
        new_turtle.goto(x=-230, y=y_position_of_first_turtle - index*30)
        all_turtles.append((new_turtle))

    if user_bet:
        is_race_on = True

    while is_race_on:

        for turtle in all_turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You win! The winner is {winning_color} turtle")
                else:
                    print(f"You lose! The winner is {winning_color} turtle")
            step_distance = random.randint(0, 10)
            turtle.forward(step_distance)

    screen.exitonclick()


if __name__ == '__main__':
    main()
