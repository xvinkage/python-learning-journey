import os
from dotenv import load_dotenv
import requests
import datetime

load_dotenv()

APP_ID = os.getenv("x-app-id")
API_KEY = os.getenv("x-app-key")
SHEETY = os.getenv("SHEETY")
AUTH = os.getenv("AUTH")

url = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
headers = {"x-app-id": APP_ID,
           "x-app-key": API_KEY,
           "Content-Type": "application/json",
           }

body = {"query": input("Enter an excercise and duration: ")
        }
response = requests.post(url=url, headers=headers, json=body)
response.raise_for_status()
result = response.json()
# print(result)

# print(result["exercises"])
today = datetime.date.today().strftime("%d/%m/%Y")
time = datetime.datetime.now().time().strftime("%H:%M:%S")

url = SHEETY
data_json = {"workout": {
                 "date": today,
                 "time": time,
                 "duration": result["exercises"][0]["duration_min"],
                 "exercise": result["exercises"][0]["name"].title(),
                 "calories": result["exercises"][0]["nf_calories"]
                 }
                 }

bearer_headers = {"Authorization": AUTH}

data = requests.post(url=url, json=data_json, headers=bearer_headers)
data.raise_for_status()
print(data.text)