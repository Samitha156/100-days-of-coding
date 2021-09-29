import requests
from datetime import datetime

USERNAME = "samitha"
TOKEN = ""
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
today = datetime.now()


graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

body = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "18",
}
graph_id = graph_config["id"]
post_endpoint = f"{graph_endpoint}/{graph_id}"


# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# response = requests.post(url=post_endpoint, json=body, headers=headers)
# print(response.text)

update_endpoint = f"{post_endpoint}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "9",
}

response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
print(response)