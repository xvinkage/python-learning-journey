import datetime as dt
import random
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL")

weekdays = [0, 1, 2, 3, 4]

now = dt.datetime.now()
day_of_week = now.weekday()


def choose_quote():
    with open("quotes.txt") as quotes_data:
        quote = quotes_data.readlines()
        random_quote = random.choice(quote)
        return random_quote.strip()


if day_of_week in weekdays:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL,
                        to_addrs=TO_EMAIL,
                        msg = f"Subject: Daily Quote\n\n{choose_quote()}")
    connection.close()
else:
    print("Weekend")
    