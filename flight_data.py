import requests
from datetime import datetime, timedelta


class FlightData:
    def __init__(self):
        self.api_key = "he25sRGsFvJBvfV5yu26YuQjkwub0LYg"
        self.api_secret = "URw99ZvDPXiUF7SV"
        self.endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"
        self.flight_search_url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        self.date = datetime.now().date()
        self.later_date = self.date + timedelta(days=30 * 2)
        self.formatted_current_date = self.date.strftime("%Y-%m-%d")
        self.formatted_later_date = self.later_date.strftime("%Y-%m-%d")

    def post_data(self):
        token_data = {
            "grant_type": "client_credentials",
            "client_id": self.api_key,
            "client_secret": self.api_secret
        }
        token_response = requests.post(url=self.endpoint, data=token_data)
        return token_response

    def get_flight_fare(self, token_response):
        headers = {
            "Authorization": f"Bearer {token_response}"
        }
        flight_search_parameters = {
            "originLocationCode": "ISB",
            "destinationLocationCode": "JED",
            "departureDate": self.formatted_later_date,
            "adults": 1,
            "travelClass": "ECONOMY",
            "currencyCode": "PKR",
            "maxPrice": 100000
        }

        data = requests.get(url=self.flight_search_url, params=flight_search_parameters, headers=headers)
        data.raise_for_status()  # Raise an exception for 4xx and 5xx HTTP status codes
        response_data = data.json()
        formatted = response_data['data'][0]['price']['total']
        print(formatted)


tempo = FlightData()
token_response = tempo.post_data()
tempo.get_flight_fare(token_response.json().get("access_token"))
