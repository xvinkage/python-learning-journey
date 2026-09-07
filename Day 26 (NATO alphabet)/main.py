import pandas as pd

data = pd.read_csv("./nato_phonetic_alphabet.csv")
nato_df = pd.DataFrame(data)

nato_dict = {row["letter"]: row["code"] for (index, row) in nato_df.iterrows()}
# print(nato_dict)

def generate_nato():
    user_input = input("Enter a word: ").upper()
    try:
        letters = [letter for letter in user_input]
        # print(letters)

        nato = [nato_dict[letter] for letter in letters]
        print(nato)
    except KeyError: 
        print("Please only enter valid letters")
        generate_nato()


generate_nato()