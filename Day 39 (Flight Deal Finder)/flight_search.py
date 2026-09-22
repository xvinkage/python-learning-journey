import os
from dotenv import load_dotenv
from requests_cache import CachedSession
from datetime import datetime, timedelta

load_dotenv()

class FlightSearch:
    def __init__(self):
        self.SERP_API = os.getenv("SERP_API")
        self.url = os.getenv("SERP_ENDPOINT")
        self.cache = CachedSession("flight_data", expire_after=900)



    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        query = {
            "api_key": self.SERP_API,
            "departure_id": origin_city_code,
            "gl": "us",
            "hl": "en",
            "adults": "2",
            "arrival_id": destination_city_code,
            "currency": "USD",
            "outbound_date": from_time.strftime("%Y-%m-%d"),
            "return_date": to_time.strftime("%Y-%m-%d"),
            "sort_by": "2"
            }
        self.response = self.cache.get(self.url, params=query)
        self.response.raise_for_status()
        self.text = self.response.text
        return self.response.json()

