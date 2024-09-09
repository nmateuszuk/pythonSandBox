def perform_calculation(num1, operator, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        elif operator == "/":
            if num2 == 0:
                raise ValueError("Cannot divide by zero")
            return num1 / num2
        else:
            raise ValueError("Invalid operator")
    except ValueError as e:
        return str(e)


continue_count = True
remember_number = 0
continue_input = "n"

while continue_count:
    if continue_input == "n":
        number_1 = input("What's the first number?: ")
    else:
        number_1 = remember_number
        print(f"Using remembered number: {number_1}")

    operator = input("Pick an operation (+ - * /): ")
    number_2 = input("What's the second number?: ")

    result = perform_calculation(number_1, operator, number_2)

    print(f"Result: {result}")

    continue_input = input(
        "Type 'e' to exit, 'y' to continue calculating with result, or 'n' to start new calculation: "
    ).lower()

    if continue_input == "y":
        remember_number = result
    elif continue_input == "n":
        remember_number = 0
        # or just rewrite to call calculator again
    elif continue_input == "e":
        print(f"Final result is {result}")
        continue_count = False
    else:
        print("Invalid input. Ending calculation.")
        continue_count = False
