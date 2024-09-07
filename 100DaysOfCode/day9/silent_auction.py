
import auction_art

continue_bidding = True

bids = {}
print(auction_art.auction)
while continue_bidding:

    name = input("What is your name?\n")
    bid = int(input("How much are you bidding? $"))

    bids[name] = bid
    bid_continue = input("Are there any other bidders. y or n\n").lower()

    if bid_continue == "n":
        continue_bidding = False

highest_bid = 0

for bidder in bids:
    bid = bids[bidder]
    if bid > highest_bid:
        highest_bid = bid
        winner = bidder
print(f"The winner is {winner} with a bid of ${highest_bid}")
