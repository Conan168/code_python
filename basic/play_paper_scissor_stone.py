import random

stone = '''
    ______
   |  ____)
---   ______)
      ______)
      ____)
----___)
'''

scissor = '''
    ______
   |  ____)_______
---   ____________)
      ____________)
      ____)
----___)
'''

paper = '''
    __________
   |  _________)
---   ____________)
      ____________)
      __________)
----_________)
'''

game_image = [stone, scissor, paper]

print('Welcom the game')
user_choice = int(input('Type "0" for stone, "1" for scissor and "2" for paper\n'))
computer_choice = random.randint(0,2)
print("Your choice: \n")
if user_choice >= 0 and user_choice <= 2:
    print(game_image[user_choice])
else:
    print("Invalid number")
print("computer choice: \n")
print(game_image[computer_choice])

if user_choice < 0 or user_choice > 2:
    print("You type a invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You lose the game!")
elif user_choice == 2 and computer_choice == 0:
    print("You win the game!")
elif user_choice < computer_choice:
    print("You win the game!")
elif user_choice == computer_choice:
    print("It is a draw!")
elif user_choice > computer_choice:
    print("You lose the game!")
