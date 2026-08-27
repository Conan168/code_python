import random

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'Q', 'R', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '%', '&', '*', '(', ')', '+']

print("welcome to python password generator!")

num_letters = int(input("How many letters would you like in your password? \n"))
num_symbols = int(input("How many symbols would you like? \n"))
num_numbers = int(input("How many numbers would you like? \n"))
use_lib = []
password = ""

for index in range(num_letters):
    letter = letters[random.randint(0,len(letters)-1)] # random.choice(letters)
    use_lib.append(letter)

for index in range(num_symbols):
    symbol = symbols[random.randint(0,len(symbols)-1)] # random.choice(symbols)
    use_lib.append(symbol)

for index in range(num_numbers):
    number = numbers[random.randint(0,len(numbers)-1)] # random.choice(numbers)
    use_lib.append(number)

random.shuffle(use_lib)

for index in use_lib:
    password += index

print(password)

