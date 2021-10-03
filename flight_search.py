import requests
from flight_data import FlightData

tequila_endpoint = "https://tequila-api.kiwi.com"
API_KEY = "ymuTmXkOXf0donahIaLgeF4D9miqAhfq"


headers = {
    "apikey": API_KEY,
}

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def find_iata(self, city_name):
        query = {
            "term": city_name,
            "location_types": "city",
        }
        response = requests.get(url=f"{tequila_endpoint}/locations/query", params=query, headers=headers)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def search_flight(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {
            "apikey": API_KEY,
        }
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP",

        }
        response = requests.get(url=f"{tequila_endpoint}/v2/search", params=query, headers=headers)
        data = response.json()["data"]
        if data:
            data = data[0]
        # pprint(data)

            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
            print(f"{flight_data.destination_city}: £{flight_data.price}")
            return flight_data




