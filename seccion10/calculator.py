# Calculator
from logo import logo
# add
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

def calculation():
    print(logo)
    num1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:

        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_fucntion = operations[operation_symbol]
        answer = calculation_fucntion(num1,num2)

        print(f"{num1} {operation_symbol} {num2} = {round(answer,2)}")

        if input(f"type 'y' to contine calculating with {answer}, or type 'n' to start a new calculation:  ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculation()
            
            
calculation()