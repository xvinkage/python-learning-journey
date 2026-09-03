print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

#  tip /100 =  tip percent
tip_percent = tip / 100
# bill *  tip percent = tip amount
tip_amount = bill * tip_percent

# total bill/people = price per person
amount_per_person = round((tip_amount + bill) / people, 2)
print(f"Each person should pay: ${amount_per_person}")