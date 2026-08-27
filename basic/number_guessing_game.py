"""It's a number guessing game"""
import random

EASY_LEVEL = 10
HARD_LEVEL = 5

def number_guessing(num, guess_times):
    """guess number n times, return win/lose"""
    high_limit = 100
    low_limit = 1

    for i in range(guess_times):
        print(f"number scope between {low_limit} to {high_limit}")
        print(f"reamining {guess_times-i} times!")
        guess = int(input("Make a guess: "))
        if guess == num:
            return f"You got the number {num}"
        if guess < low_limit or guess > high_limit:
            continue

        if guess > num:
            high_limit = guess
        else:
            low_limit = guess

    return f"You lose. The number is {num}"


def main():
    """main"""
    print(
        "Welcome to the number guessing game!! \n" \
        "I'm thinking of a number between 1 to 100."
    )

    should_continue = True
    while should_continue:
        boom = random.randint(1, 100)

        level = input("choose a level of difficulty. Type 'easy' or 'hard': ").lower()

        if level == "easy":
            times = EASY_LEVEL
            print(number_guessing(boom, times))
            user_continue = input("Next round. Type 'y' or 'n'! ").lower()
            if user_continue == "y":
                print("\n"*50)
            else:
                should_continue = False
        elif level == "hard":
            times = HARD_LEVEL
            print(number_guessing(boom, times))
            user_continue = input("Next round. Type 'y' or 'n'! ").lower()
            if user_continue == "y":
                print("\n" * 50)
            else:
                should_continue = False
        else:
            print("Please Type 'easy' or 'hard'")
            should_continue = False

if __name__ == '__main__':
    main()
