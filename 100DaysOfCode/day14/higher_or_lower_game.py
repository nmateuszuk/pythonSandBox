import random
from data import data
from art_logo import logo
from art_vs import versus


def get_random_data():
    return random.choice(data)


def print_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"


def game():
    print(logo)
    score = 0
    continue_game = True

    account_a = get_random_data()
    account_b = get_random_data()
    correct_answer = account_b

    while continue_game:
        print(f"-------round {score + 1}-------")
        account_a = correct_answer
        account_b = get_random_data()

        while account_a == account_b:
            account_b = get_random_data()

        print(f"Compare A: {print_data(account_a)}.")
        print(versus)
        print(f"Against B: {print_data(account_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        if a_follower_count > b_follower_count and guess == "a":
            correct_answer = account_a
            score += 1
            print(f"You're right! Current score: {score}.")
        elif a_follower_count < b_follower_count and guess == "b":
            correct_answer = account_b
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            continue_game = False
            print(f"Sorry, that's wrong. Final score: {score}")


game()

# alternative
# def check_answer(guess, a_followers, b_followers):
#     """Checks followers against user's guess
#     and returns True if they got it right.
#     Or False if they got it wrong."""
#     if a_followers > b_followers:
#         return guess == "a"
#     else:
#         return guess == "b"
