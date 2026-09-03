import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_input = int(input("What do you Choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
choices = [rock, paper, scissors]


def win():
    print("You win")


if user_input > 2 or user_input < 0:
    print("Invalid choice")
    quit()
user_choice = choices[user_input]

computer_pick = random.randint(0, 2)
computer_choice = choices[computer_pick]
print(user_choice)
print(f"computer choose: {computer_choice}")
if user_input == 0 and computer_pick == 2:
    win()
elif user_input == 1 and computer_pick == 0:
    win()
elif user_input == 2 and computer_pick == 1:
    win()
elif user_input == computer_pick:
    print("Draw")
else:
    print("You lose:")