import os
from dotenv import load_dotenv
from requests_cache import CachedSession
import requests

load_dotenv()

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.SHEET = os.getenv("SHEETY_URL")
        self.SHEETY_AUTH = os.getenv("SHEETY_AUTH")
        self.cache = CachedSession("data_manager", expire_after=0)

    def get_destination_data(self):
        auth_header = {"Authorization": self.SHEETY_AUTH}
        self.response = self.cache.get(self.SHEET,headers=auth_header)
        data = self.response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_lowest_price(self, row_id, new_price):
        row_data = {"price": {
            "lowestPrice": new_price
            }}
        auth_header = {"Content-Type": "application/json",
                       "Authorization": self.SHEETY_AUTH}

        response = requests.put(f"{self.SHEET}/{row_id}", json=row_data, headers=auth_header)
        # response.raise_for_status()
        print(response.status_code)
        print(response.text)
        print(f"{self.SHEET}/{row_id}")

