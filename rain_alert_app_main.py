import requests
from twilio.rest import Client

account_sid = "AC22a576bf0fa38cb70e45832024b35bfc"
auth_token = "a31c571d216eb6fe82441cd51b378423"

parameters = {
    "lat": 41.0814,
    "lon": -81.519,
    "appid": "064952df85195c62fbea7be33dbe8446",
    "exclude": "current,minutely,daily"
}

# api_key = "064952df85195c62fbea7be33dbe8446"

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()
# print(data)
# print(response.status_code)

# for i in range(13):
#     for weather_id in data["hourly"][i]["weather"]:
#         if int(weather_id["id"]) < 700:
#             print(f"Bring an Umbrella")
#         else:
#             print(int(weather_id["id"]))

weather_slice = data["hourly"][:12]

will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an Umbrella",
        from_='+19286156986',
        to='+13303226254'
    )
    print(message.status)
#     print("Bring an Umbrella")
# # print(data["hourly"][0]["weather"][0]["id"])



