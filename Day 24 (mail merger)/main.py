letter_file = "./Input/Letters/starting_letter.txt"
name_file = "./Input/Names/invited_names.txt"


with open(letter_file) as letter, open(name_file) as name:
    content_letter = letter.read()
    names_list = name.readlines()
    # print(names_list)

    for person in names_list:
        name_clean = person.strip()
        new_letter = content_letter.replace("[name]", name_clean)
        output_file = f"./Output/ReadyToSend/letter_for_{name_clean}.txt"

        with open(output_file, mode="w") as output:
        # print(new_letter)
            output.write(new_letter)


