import random
from number_guessing_logo import logo


def check_a_number(number_to_guess, guess) -> bool:
    if number_to_guess > guess:
        print("too low!")
        return False
    elif number_to_guess < guess:
        print("too high!")
        return False
    return True


def game():
    attempts = 0

    print(logo)
    print("Welcome to the Number Guesing Game!")
    print("I'm thinking af a number between 1 and 100")

    number_to_guess = random.randint(1, 100)

    difficulty = input(
        "Choose a difficulty. type 'e' for easy or 'h' for hard: ").lower()
    if difficulty == "e":
        attempts = 10
    else:
        attempts = 5

    while attempts > 0:
        print(f"You have {attempts} left to guess the number")
        guess_input = input("Make a guess: ")
        if (not guess_input.isnumeric()):
            print("guess is not a number")
            continue

        guess = int(guess_input)
        win = check_a_number(number_to_guess, guess)
        if win:
            print("YOU WIN!")
            break
        else:
            attempts -= 1


game()
