import requests
from datetime import datetime

GENDER = "Male"
WEIGHT_KG = 68
HEIGHT_CM = 167
AGE = 30

APP_ID = "XXXX"
API_KEY = "XXX"
neutrition_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/26ec10a91c8b576f4d4dde0d6a7aa4f2/myWorkouts/workouts"

exercise_text = input("Tell me which exercise you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

body = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}



response = requests.post(url=neutrition_endpoint, json=body, headers=headers)
results = response.json()
print(results)

today = datetime.now()
DATE = today.strftime("%m/%d/%Y")
TIME = today.strftime("%H:%M:%S")

bearer_headers = {
    "Authorization": f"Bearer fhuina1512jk"
}

for exercise in results["exercises"]:
    sheety_params = {
        "workout": {
            "date": DATE,
            "time": TIME,
            "exercise": exercise["name"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    # # With Basic Authentication
    # sheety_post = requests.post(url=sheety_endpoint, json=sheety_params, auth=("samithaforloop", "07572300Ss@@"))
    # post_results = sheety_post.text
    # print(post_results)

    #Bearer Token Authentication
    sheet_response = requests.post(
        url=sheety_endpoint,
        json=sheety_params,
        headers=bearer_headers
    )
    print(sheet_response.text)