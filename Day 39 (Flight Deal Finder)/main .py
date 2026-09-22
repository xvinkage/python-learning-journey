from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from flight_data import FlightData
import smtplib
import os
from dotenv import load_dotenv



sheet_data = DataManager()
# print(sheet_data.text)
datasheet = sheet_data.get_destination_data()
# destinations = [IATA["iataCode"] for IATA in datasheet]

# print(destinations)
tomorrow = datetime.now() + timedelta(days=60)
six_month_from_today = datetime.now() + timedelta(days=(63))
# IATA_code = datasheet[0]["lowestPrice"]

for IATA in datasheet:
    destination = IATA["iataCode"]

    flight_search = FlightSearch()
    flights = flight_search.check_flights(origin_city_code="ROC",
                                destination_city_code=destination,
                                from_time=tomorrow,
                                to_time=six_month_from_today)

# print(flight_search.text) #prints json so i can use viewer

    flight_data = FlightData(price = flights["other_flights"][0]["price"],
                            origin_airport= flights["other_flights"][0]["flights"][0]["departure_airport"]["id"],
                            destination_airport= flights["other_flights"][0]["flights"][0]["arrival_airport"]["id"],
                            out_date= flights["other_flights"][0]["flights"][0]["departure_airport"]["time"].split(" ")[0],
                            return_date= six_month_from_today,
                            )


    cheapest_flight = flight_data.find_cheapest_flight(flight_data)
    # print("Flight price:", cheapest_flight)
    # print("Sheet price:", IATA["lowestPrice"])
    # print("Row ID:", IATA["id"])



    if cheapest_flight.price != "N/A" and cheapest_flight.price < IATA["lowestPrice"]:
        sheet_data.update_lowest_price(IATA["id"], cheapest_flight.price)

        load_dotenv()
        MY_EMAIL = os.getenv("MY_EMAIL")
        MY_PASSWORD = os.getenv("MY_PASSWORD")

        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=MY_EMAIL, 
                         password=MY_PASSWORD)
        
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Low price alert! only ${cheapest_flight.price} to fly from {flight_data.origin_airport} to {IATA["iataCode"]} 
                            from {flight_data.out_date} to {flight_data.return_date.strftime("%Y-%m-%d")}")