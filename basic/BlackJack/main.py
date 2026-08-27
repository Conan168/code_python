"""A program of blackjack game"""
import random

def deal_card():
    """Return a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_cards(cards):
    """take a list of cards and return score of calculate cards"""
    if sum(cards) == 21 and len(cards) ==2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_scores, computer_scores):
    """compare user's score and computer's score to know if user is winner"""
    if user_scores == computer_scores:
        return "draw"
    elif computer_scores == 0:
        return "Your opponent have blackjack, you lose!"
    elif user_scores == 0:
        return "Win with blackjack"
    elif user_scores > 21:
        return "You went over. You lose!"
    elif computer_scores > 21:
        return "Your opponent went over. You win!"
    elif user_scores > computer_scores:
        return "You win the game"
    else:
        return "You lose the game"

def play_blackjack():
    """run blackjack"""
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_cards(user_cards)
        computer_score = calculate_cards(computer_cards)

        print(f'your cards is {user_cards}, score is {user_score}')
        print(f'computer cards is {computer_cards[0]}')

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_chould_enter = input(
                'Type "y" to get another card, type "n" to pass the round: '
            ).lower()
            if user_chould_enter == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_cards(computer_cards)
        print(f'computer cards is {computer_cards}, score is {computer_score}')

    print(f'your cards is {user_cards}, score is {user_score}')
    print(f'computer cards is {computer_cards}, score is {computer_score}')
    print(compare(user_score, computer_score))

def main():
    """main function"""
    next_game = True

    while next_game:
        should_next = input(
            "Do you want to play blackjack. Type 'y' to start, type 'n' to stop\n"
        ).lower()
        if should_next == "y":
            print("\n" * 50)
            play_blackjack()
        else:
            next_game = False

if __name__ == '__main__':
    main()
