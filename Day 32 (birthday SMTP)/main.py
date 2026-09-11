import datetime as dt
import pandas as pd
import random
import smtplib
import os 
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("PASSWORD")

df = pd.read_csv("birthdays.csv", usecols=["name", "email", "year", "month", "day"])

now = dt.datetime.now()
now_day = now.day
now_month = now.month

birthday_dict = df.to_dict(orient="records")

def birthday():
    for birthday in birthday_dict:
        if now_month == birthday["month"]:
            if now_day == birthday["day"]:
                print("found")
                number = random.randint(1, 3)
                letter_path = f"letter_templates/letter_{number}.txt"

                with open(letter_path) as file:
                    birthday_letter = file.read()
                    updated_letter = birthday_letter.replace("[NAME]", birthday["name"])

                    connection = smtplib.SMTP("smtp.gmail.com")
                    connection.starttls()
                    connection.login(user= MY_EMAIL, password=PASSWORD)
                    connection.sendmail(from_addr=MY_EMAIL,
                                        to_addrs=birthday["email"],
                                        msg= f"Subject: Happy Birthday {birthday["name"]}\n\n{updated_letter}")
                    connection.close()
                    print(f"Email sent to {birthday["name"]}")

birthday()




