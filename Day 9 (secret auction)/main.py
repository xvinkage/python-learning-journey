import art

print(art.logo)
bidding = True


def clear_input():
    print("\n" * 50)


bids = {}


while bidding:
    user_name = input("What is your name? ")
    user_bid = int(input("What is your bid? $"))

    bids[user_name] = user_bid
    # print(bids)
    additional_bids = input("Are there any other bidders? Type 'yes' or 'no'").lower()

    if additional_bids == "yes":
        clear_input()
        bidding = True
    elif additional_bids == "no":
        bidding = False
        # print("no")
winner = max(bids, key=bids.get)
winning_bet = bids[winner]
print(f" The winner is {winner} with a bet of {winning_bet}")

