import requests
from flight_search import IATA_CODE_FINDER

city_name = input("Enter City Name: ")
iata_finder = IATA_CODE_FINDER(city_name)
post_data_sheets = {
    "price": {
        "city": city_name,
        "iataCode": iata_finder.iata_get_method(),
        "lowestPrice": 56
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

temp = DataManager()
temp.post_method()
