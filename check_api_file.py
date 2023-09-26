import requests
import json
from datetime import datetime, timedelta

API_KEY = "he25sRGsFvJBvfV5yu26YuQjkwub0LYg"
API_SECRET = "URw99ZvDPXiUF7SV"
api_endp = "https://test.api.amadeus.com/v1/security/oauth2/token"

# Request an access token
token_data = {
    "grant_type": "client_credentials",
    "client_id": API_KEY,
    "client_secret": API_SECRET
}

token_response = requests.post(url=api_endp, data=token_data)

if token_response.status_code == 200:
    access_token = token_response.json().get("access_token")
else:
    print(f"Error requesting access token: {token_response.status_code}")
    exit()

# Use the access token to make a flight search request
flight_search_url = "https://test.api.amadeus.com/v2/shopping/flight-offers"

flight_search_parameters = {
    "originLocationCode": "ISB",
    "destinationLocationCode": "JED",
    "departureDate": "2023-10-02",
    "adults": 1,
    "travelClass": "ECONOMY",
    "currencyCode": "PKR",
    "maxPrice": 100000
}

headers = {
    "Authorization": f"Bearer {access_token}"
}

data = requests.get(url=flight_search_url, params=flight_search_parameters, headers=headers)
form = data.json()
formatted = form['data'][0]['price']['total']
print(formatted)

date = datetime.now().date()
later_date = date + timedelta(days=30 * 2)
formatted_current_date = date.strftime("%Y-%m-%d")
formatted_later_date = later_date.strftime("%Y-%m-%d")
print(formatted_later_date)
