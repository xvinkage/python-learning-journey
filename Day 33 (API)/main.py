import requests
from datetime import datetime
import smtplib
import os
from dotenv import load_dotenv
import time

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude


iss_latitude = ""
iss_longitude = ""


#Your position is within +5 or -5 degrees of the ISS position.
def iss_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    global iss_longitude, iss_latitude
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5:
        if MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
            return True


parameters = {

    "lat": MY_LAT,
    "lng": MY_LONG,
}

response = requests.get("https://api.sunrise-sunset.org/v2", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

while True:
    time.sleep(60)
    position = iss_position()
    if position == True:
        if time_now.hour >= sunset or time_now.hour < sunrise:    
            load_dotenv()
            MY_EMAIL = os.getenv("MY_EMAIL")
            MY_PASSWORD = os.getenv("MY_PASSWORD")

            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg="Subject: ISS OVERHEAD\n\nLOOK UP!")
    else:
        print(f"Not close\nLat: {iss_latitude}\nLong:{iss_longitude}")


