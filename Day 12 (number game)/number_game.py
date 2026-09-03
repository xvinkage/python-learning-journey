import random

difficulties = {
    "easy": 10,
    "hard": 5,
}


def difficulty(choice):
    return difficulties[choice]


def guess(guess_numb, number):
    if guess_numb < number:
        return "Too low."
    elif guess_numb > number:
        return "Too high."
    else:
        return "Correct"


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
number = random.randint(1, 100)
# print(number)

choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = difficulty(choice)

print(f"You have {attempts} remaining to guess the number ")
while attempts >= 1:

    guess_numb = int(input("Make a guess: "))
    result = guess(guess_numb, number)
    # if ATTEMPTS == 0:
    if result == "Too low.":
        attempts -= 1
        print(result)
        print(f"You have {attempts} remaining to guess the number ")
    elif result == "Too high.":
        attempts -= 1
        print(result)
        print(f"You have {attempts} remaining to guess the number ")
    elif result == "Correct":
        print(f"You got it! the answer was {number}")
        break
    if attempts == 0:
        print(f"You've run out of guesses. The answer was {number}")
