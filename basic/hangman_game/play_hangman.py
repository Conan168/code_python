import random
import create_word_list

chosen_word = random.choice(create_word_list.world_list)
print(chosen_word)
print("_ " * len(chosen_word))

lives = 100
letter_list = []
CORRECT = False

while  not CORRECT:
    display = ""
    guess = input("Guess a letter:\n").lower()

    if guess not in chosen_word:
        lives -= 20
        print(f'!!!Lives: {lives}')
        if lives == 0:
            print(f'*********************The word is "{chosen_word}". Game over*********************')
            CORRECT = True

    else:    
        for letter in chosen_word:
            if letter == guess:
                display += letter
                letter_list.append(letter)
            elif letter in letter_list:
                display += letter
            else:
                display += "_ "
        print(display)
        print(f'!!!Lives: {lives}')

        if "_" not in display:
            CORRECT = True
            print("*********************You win*********************")


