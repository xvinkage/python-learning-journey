import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

dealer_total = 0
user_total = 0


def deal(user_or_dealer, amount_cards=1):
    cards_dealt = (random.sample(cards, k=amount_cards))
    user_or_dealer.extend(cards_dealt)
    return cards_dealt


def calculate_score(user_or_dealer):
    while sum(user_or_dealer) > 21 and 11 in user_or_dealer:
        user_or_dealer.remove(11)
        user_or_dealer.append(1)
    return sum(user_or_dealer)


def hit_or_stand(user_or_dealer):
    hit = True
    while hit:
        choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        if choice == 'y':
            deal(user_or_dealer)

            print(f"Your cards: {user_or_dealer}, current score: {calculate_score(user_or_dealer)}")

            if calculate_score((user_or_dealer)) > 21:
                hit = False
                return "YOU BUSTED! YOU LOSE"

            if calculate_score(user_or_dealer) == 21:
                hit = False
                return "YOU WIN!"

            # total = calculate_score(user_or_dealer)
        # print(total)
        if choice == 'n':
            hit = False


def dealer_turn(dealer):
    dealer_score = calculate_score(dealer)

    while dealer_score < 17:
        deal(dealer)
        dealer_score = calculate_score(dealer)


def compare_score():
    dealer_score = calculate_score(dealer)
    user_score = calculate_score(user)
    if user_score > 21:
        return f"YOU LOSE, DEALER WINS"
    elif dealer_score > 21:
        return f"DEALER BUST, YOU WIN!"
    elif user_score > dealer_score:
        return f"YOU WIN, DEALER LOSES"
    elif dealer_score > user_score:
        return f"YOU LOSE, DEALER WINS"
    elif dealer_score == user_score:
        return f"DRAW"


start_game = True

while start_game:
    dealer = []
    user = []
    play = input("Do you want to play a game of Blackjack Type 'y' or 'n': ").lower()
    if play == 'y':
        print("\n" * 50)
        print(art.logo)
        deal(user, 2)
        deal(dealer, 2)
        dealer_total = calculate_score(dealer)
        print(f"Your cards: {user}, current score: {calculate_score(user)}")
        print(f"Dealer's first card: {dealer[0]}")
        if len(dealer) == 2 and sum(dealer) == 21:
            print("BLACK JACK")
            start_game = False
            continue

        if len(user) == 2 and sum(user) == 21:
            print("BLACK JACK")
            start_game = False

        elif calculate_score(user) < 21:
            result = hit_or_stand(user)

            if result == "YOU WIN!":
                print(f"Your final hand: {user}, final score: {calculate_score(user)}")
                print(f"Dealer's final hand: {dealer}, final score: {calculate_score(dealer)}")
                print(result)
                start_game = False

            elif result == "YOU BUSTED! YOU LOSE":
                print(f"Your final hand: {user}, final score: {calculate_score(user)}")
                print(f"Dealer's final hand: {dealer}, final score: {calculate_score(dealer)}")
                print(result)
                start_game = False

            else:
                dealer_turn(dealer)
                print(f"Your final hand: {user}, final score: {calculate_score(user)}")
                print(f"Dealer's final hand: {dealer}, final score: {calculate_score(dealer)}")
                print(compare_score())

    if play == 'n':
        start_game = False
