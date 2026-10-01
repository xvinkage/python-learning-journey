import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import smtplib
from email.message import EmailMessage

practice_url = "https://appbrewery.github.io/instant_pot/"
real_url = "https://www.amazon.com/dp/B0FHJ7TKZM?ref_=MARS_NAVSTRIPE_desktop_ring_doorbell_batt&th=1"
target_price = 100

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36",
           "Accept-Language": "en-US,en-GB;q=0.9,en;q=0.8",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", 
           }

response = requests.get(real_url, headers=headers)
data = response.content

soup = BeautifulSoup(data, "html.parser")
dollars = soup.select_one("span.a-price-whole").text
cents = soup.select_one("span.a-price-fraction").text

item = soup.select_one("span#productTitle").text
print(item)

price = float(dollars+cents)
print(price)

if price < target_price:
    load_dotenv()
    MY_EMAIL = os.getenv("MY_EMAIL")
    MY_PASSWORD = os.getenv("MY_PASSWORD")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        message = EmailMessage()
        message["Subject"] = "Amazon Price Alert!"
        message["From"] = MY_EMAIL
        message["To"] = MY_EMAIL

        message.set_content(
            f"{item} is now {price}\n{practice_url}"
        )
        connection.send_message(message)
        print("Email successfully sent")