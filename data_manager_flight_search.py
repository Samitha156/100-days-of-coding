import requests

sheet_endpoint = "https://api.sheety.co/26ec10a91c8b576f4d4dde0d6a7aa4f2/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def get_destination_data(self):
        sheet_values = requests.get(url=sheet_endpoint)
        sheet_dict = sheet_values.json()
        return sheet_dict["prices"]

    def update_sheet(self, sheet):
        for row in sheet:
            id = row["id"]
            put_endpoint = f"{sheet_endpoint}/{id}"
            # print(put_endpoint)
            update_params = {
                "price": {
                    "iataCode": row["iataCode"]
                }
            }
            response = requests.put(url=put_endpoint, json=update_params)
            print(response.text)

