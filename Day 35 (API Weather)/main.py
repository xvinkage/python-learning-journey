import requests
import os
from dotenv import load_dotenv
# from twilio.rest import Client
import smtplib


load_dotenv()
AUTH = os.getenv("API_KEY")
SID = os.getenv("SID")
CLIENT_SECRET = os.getenv("client_secret")
# MY_NUMBER = os.getenv("MY_NUMBER")
# FROM_NUMBER = os.getenv("FROM_NUMBER")
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")
NUMBER_EMAIL = os.getenv("NUMBER")


url = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {"lat": 42.39,
              "lon": -93.40,
              "appid": AUTH,
              "cnt": 4,
              }

response = requests.get(url, params=parameters)
response.raise_for_status()
print(response)
weather_data = response.json()
# weather_id = weather_data["list"][0]["weather"]
weathers = [id["weather"][0]["id"] for id in weather_data["list"]]

will_rain = False
for num in weathers:
    if num < 600:
        will_rain = True
if will_rain:
    print("Sending Email...")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=NUMBER_EMAIL, msg="It's going to rain today, bring an umbrella")
        print("Email successfully sent!")

#     client = Client(SID, CLIENT_SECRET)
#     message = client.messages.create(
#     body="Bring an umbrella, it might rain",
#     from_=FROM_NUMBER,
#     to=MY_NUMBER,
# # )
#     print(message.body)
#     print(message.status)
