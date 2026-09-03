import random
import art
import game_data

score = 0
print(art.logo)


def pick_accounts():
    """Randomly chooses 2 accounts from dictionary
     and returns the dictionary for that account"""
    accounts = random.sample(game_data.data, k=2)
    return accounts


def compare():
    choice = input("Who has more followers? 'A' or 'B'").upper()
    if choice == 'A':
        if account_a["follower_count"] > account_b["follower_count"]:
            return account_a
        else:
            return None

    if choice == 'B':
        if account_b["follower_count"] > account_a["follower_count"]:
            return account_b
        else:
            return None


playing = True
accounts = pick_accounts()
account_a = accounts[0]
account_b = accounts[1]

while playing:
    print(f"Compare A: {account_a["name"]}, {account_a["description"]}, from {account_a["country"]}")
    print(art.vs)
    print(f"Compare B: {account_b["name"]}, {account_b["description"]}, from {account_b["country"]}")
    result = compare()

    if result == account_a or result == account_b:
        score += 1
        print("\n" * 20)
        print(f"You're right! Score: {score}")
        account_a = result
        accounts = pick_accounts()
        account_b = accounts[1]
        if account_a == account_b:
            account_b = accounts[0]
    else:
        playing = False
        print(f"Sorry, that's wrong. Final score: {score}")
