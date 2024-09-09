import random


card_symbols = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
card_values = ['Ace', '2', '3', '4', '5', '6',
               '7', '8', '9', '10', 'Jack', 'Queen', 'King']

deck = []
for symbol in card_symbols:
    for value in card_values:
        deck.append((value, symbol))

# deck = [(card, symbol) for symbol in card_symbol for card in cards_list]


def card_value(card):
    if card[0] in ['Jack', 'Queen', 'King']:
        return 10
    elif card[0] == 'Ace':
        return 11
    else:
        return int(card[0])


def sum_player_deck(cards):
    cards_sum = sum(card_value(card) for card in cards)
    if cards_sum <= 21:
        return cards_sum

    for card in cards:
        if card[0] == "Ace":
            return cards_sum-10

    return cards_sum


random.shuffle(deck)
player_card = [deck.pop(), deck.pop()]
dealer_card = [deck.pop(), deck.pop()]

while True:
    player_score = sum_player_deck(player_card)
    dealer_score = sum_player_deck(dealer_card)

    print("players cards: ", player_card)
    print("players score: ", player_score)

    if player_score == 21:
        break

    continue_game = input("'c' for card, 's' to stop: ").lower()

    if continue_game == "c":
        card = deck.pop()
        player_card.append(card)
    elif continue_game == "s":
        break
    else:
        print("Provide valid choice")
        continue
    player_score = sum_player_deck(player_card)
    if player_score > 21:
        break

while dealer_score < 17:
    card = deck.pop()
    dealer_card.append(card)
    dealer_score = sum_player_deck(dealer_card)

print("Cards Dealer Has:", dealer_card)
print("Score Of The Dealer:", dealer_score)
print("\n")

if player_score > 21:
    print("players cards: ", player_card)
    print("players score", player_score)
    print("above 21, game over, busted")
    print("dealer wins, dealer score", dealer_score)
    print("\n")
elif dealer_score > 21:
    print("Score Of The Dealer:", dealer_score)
    print("Score Of The Player:", player_score)
    print("Player wins, dealer busted")
elif player_score > dealer_score:
    print("Score Of The Dealer:", dealer_score)
    print("Score Of The Player:", player_score)
    print("Player wins")
elif dealer_score > player_score:
    print("Score Of The Dealer:", dealer_score)
    print("Score Of The Player:", player_score)
    print("Dealer wins")
else:
    print("Score Of The Dealer:", dealer_score)
    print("Score Of The Player:", player_score)
    print("It's a draw.")
