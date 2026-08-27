def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator(num):
    for symbol in operations:
        print(symbol)

    operation_symbol = input('Enter your operation\n' )
    second_number = float(input("Enter your second number.\n"))
    answer = operations[operation_symbol](num, second_number)
    print(f'{num} {operation_symbol} {second_number} = {answer}')
    return answer

def main():
    should_continue = True

    first_number = float(input("Enter your first number.\n"))
    
    while should_continue:
        answer = calculator(first_number)
        yes_or_no = input(f'Type "Y" to continue calculating with {answer}. Or "N" to restart \n').lower()
        if yes_or_no == "y":
            first_number = answer
        elif yes_or_no == "n":
            should_continue = False
            print("\n"*100)
            main()

if __name__ == '__main__':
    main()