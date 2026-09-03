name1 = input("What is your name?")
name2 = input("What is your lover's name?")

true_g = "true"
love = "love"
def calculate_love_score(name1, name2):
    lovers = name1 + " " + name2
    count = 0
    count_2 = 0
    for letter in lovers:
        if letter in true_g:
            count += 1
        if letter in love:
            count_2 += 1
    # print(f"{count} times")
    # print(f"{count_2} times")
    
    love_score = print("Love Score:", str(count) + str(count_2))


calculate_love_score(name1, name2)