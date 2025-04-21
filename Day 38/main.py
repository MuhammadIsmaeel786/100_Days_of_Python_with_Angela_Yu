import requests
from datetime import datetime
import os

USERNAME = "ismaeel"
PASSWORD = os.environ.get("ENV_SHEETY_PASSWORD")
APP_ID = os.environ.get("ENV_NIX_APP_ID")
API_KEY = os.environ.get("ENV_NIX_API_KEY")
# SHEETY_ENDPOINT_TOKEN = os.environ.get("ENV_SHEETY_TOKEN")
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")
sheety_endpoint = "https://api.sheety.co/aa4766c93a6ae6363289d4aecf46e61b/myWorkouts/workouts"

headers ={
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

today_date = datetime.now().strftime('%d/%m/%Y')
now_time = datetime.now().strftime('%X')
print(today_date)
exercise_params ={
    "query": exercise_text,
    "weight_kg": 85,
    "height_cm": 175,
    "age": 25,
    "gender": "male"
}

response =  requests.post(exercise_endpoint, headers=headers, json=exercise_params)
result = response.json()
for exercise in result["exercises"]:
    sheet_data = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    # bearer_headers = {
    #     "Authorization": f"Bearer {}"
    # }
    # sheet_response = requests.post(
    #     sheet_endpoint,
    #     json=sheet_inputs,
    #     headers=bearer_headers
    # )
    sheet_response = requests.post(url=sheety_endpoint,json=sheet_data,auth=(USERNAME,PASSWORD))
    print(sheet_response.text)