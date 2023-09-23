import requests


# -----------------

class IATA_CODE_FINDER:

    def __init__(self, city_name):
        self.api_key = "oEw443JV2r6fO6PNVfpESvUxA8Djr05_"
        self.city_name = city_name
        self.api_end_point = "https://api.tequila.kiwi.com/locations/query"

    def iata_get_method(self):
        headers = {
            "apikey": self.api_key
        }
        parameters = {
            "term": self.city_name,
            "location_types": "city"
        }
        response = requests.get(url=self.api_end_point, headers=headers,
                                params=parameters)
        data = response.json()["locations"]
        code_data = data[0]["code"]

        return code_data


