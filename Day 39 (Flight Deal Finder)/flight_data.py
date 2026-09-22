from flight_search import FlightSearch

class FlightData:
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date

    
    

    def find_cheapest_flight(self, data):
        if data is None:
            print("No flight data")
            return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")
        return FlightData(self.price,
                          self.origin_airport,
                          self.destination_airport,
                          self.out_date,
                          self.return_date
                          )

    