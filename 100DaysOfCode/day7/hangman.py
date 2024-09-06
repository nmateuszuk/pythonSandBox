import random
from hangman_words_list import words
from hangman_stages import hangman_stages

placeholder_list = list()
hangman_lost_lives = 0


def generate_word():
    index = random.randint(0, len(words)-1)
    print(words[index])
    return words[index]


def placeholder_init(word):
    for _ in range(0, len(word)):
        placeholder_list.append("_")
    print(placeholder_list)


def guess_a_letter():
    letter = input("Guess a letter \n").lower()
    return letter


def check_letter(word, letter):
    global hangman_lost_lives  # Declare hangman_lost_lives as global
    index = 0
    found = False
    for let in word:
        if let == letter:
            placeholder_list[index] = let
            found = True
        index += 1

    if not found:
        hangman_lost_lives += 1
    print("".join(placeholder_list))


def check_status():
    if "_" not in placeholder_list:
        print("You")
        return True
    return False


game_over = False


new_word = generate_word()
placeholder_init(new_word)

while not game_over or hangman_lost_lives == 6:
    letter = guess_a_letter()
    check_letter(new_word, letter)

    print(hangman_stages[hangman_lost_lives])
    game_over = check_status()
