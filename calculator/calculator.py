
#Functions
def add(n1, n2):
    return n1 + n2;

def subtract(n1, n2):
    return n1 - n2;

def multiply(n1, n2):
    return n1 * n2;

def divide(n1, n2):
    return n1 / n2;

operations = {
    "-": subtract,
    "+": add,
    "*": multiply,
    "/": divide,
}

def calculator():
    continue_calculation = True
    num1 = float(input("Enter the first number: "))

    for operation in operations:
            print(operation)

    while continue_calculation:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("Enter the next number: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculation with {answer} or 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            continue_calculation = False
            calculator()
calculator()