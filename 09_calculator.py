from ascii_art import calculator_logo

def calculate():
    '''
    :return: returns the sum, difference, product, or dividend of the two numbers the user selects
    '''
    # print the logo to the user at the start of the game
    print(calculator_logo)
    # variable for storing answer for multiple calculations
    answer = 0
    # boolean to continue using the program
    calculating = True
    # variable for determining continuous state of game
    go_again = 'n'

    # while the user doesn't stop
    while calculating:
        # prompt the user for the first number
        if go_again == 'n':
            number1 = float(input("What's the first number?: "))
        # prompt the user for the operation
        operation = input("+\n-\n*\n/\nPick an operation: ")
        # prompt the user for the second number
        number2 = float(input("What is the second number?: "))

        # perform the calculation accordingly and save to answer variable
        if operation == "+":
            answer = number1 + number2
        elif operation == "-":
            answer = number1 - number2
        elif operation == "*":
            answer = number1 * number2
        else:
            answer = number1 / number2

        # print the result to the user
        print(f"{number1} {operation} {number2} = {answer}\n")

        go_again = input(f"Type 'y' to continue calculating with {answer}, or type 'n'"
                         f" to start a new calculation, or type 'q' to quit: ")
        if go_again == 'y':
            number1 = answer
        elif go_again == 'q':
            calculating = False


# calculate()


# Second method of creating calculator function using dictionary

# define the 4 mathematical operations to use
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

# create a dictionary for the functions and their corresponding operation symbol
operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

# use dictionary operations to perform calculations
numb1 = 8
numb2 = 3
operation = "*"
print(operations[operation](numb1, numb2))