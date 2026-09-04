import pandas as pd

data = pd.read_csv("./nato_phonetic_alphabet.csv")
nato_df = pd.DataFrame(data)

nato_dict = {row["letter"]: row["code"] for (index, row) in nato_df.iterrows()}
# print(nato_dict)

user_input = input("Enter a word: ").upper()

letters = [letter for letter in user_input]
# print(letters)

nato = [nato_dict[letter] for letter in letters if nato_dict[letter]]
print(nato)