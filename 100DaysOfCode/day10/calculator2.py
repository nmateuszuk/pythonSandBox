
def add(num1, num2):
    return num1+num2


def substract(num1, num2):
    return num1-num2


def multiply(num1, num2):
    return num1*num2


def divide(num1, num2):
    return num1/num2


operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}

print(operations["*"](2, 3))

operation_symbol = "+"
answer = operations[operation_symbol](2, 3)
