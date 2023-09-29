import requests
from flight_search import IATA_CODE_FINDER
from flight_data import FlightData
from datetime import datetime

# ====================Objects for Flight Fare===============
get_fare = FlightData()
token_response = get_fare.post_data()
access_token = token_response.json().get("access_token")
fare = get_fare.get_flight_fare(access_token)
# ==========================================================


city_name = "Jeddah"
iata_finder = IATA_CODE_FINDER(city_name)
post_data_sheets = {
    "price": {
        "city": city_name,
        "iataCode": iata_finder.iata_get_method(),
        "lowestPrice": fare

    }
}


# ---------------------------------------------------------

class DataManager:
    headers_sheets = {
        "Authorization": "Basic aGVpZ2h0ZXI6QWxsYWg3ODY2Ng",
        "Content-Type": "application/json"
    }

    def __init__(self):
        self.get_api = "https://api.sheety.co/5fafca3848db139085b97ac615be33bb/flightClub/prices"
        self.post_api = "https://api.sheety.co/5fafca3848db139085b97ac615be33bb/flightClub/prices"

    def get_method(self):
        response = requests.get(url=self.get_api, headers=DataManager.headers_sheets)
        data = response.json()
        print(data)

    def post_method(self):
        response = requests.post(url=self.post_api, headers=DataManager.headers_sheets,
                                 json=post_data_sheets)  # Use the defined post_data_sheets
        data = response.status_code
        print(data)


update_sheet = DataManager()
update_sheet.post_method()
