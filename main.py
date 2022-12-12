import requests
from datetime import datetime
import os

# nutritionix info
APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
params = {
    "query": input("What did you do today? "),
    "gender": "male",
    "weight_kg": your weight,
    "height_cm": your height,
    "age": your age,
}
response = requests.post(url=ENDPOINT, json=params, headers=header)
response.raise_for_status()
result = response.json()

workout_name = result["exercises"][0]["name"].title()
duration_min = result["exercises"][0]["duration_min"]
calories_burned = result["exercises"][0]["nf_calories"]

# get the current date
today = datetime.now().strftime("%d/%m/%Y")
local_time = datetime.now().strftime("%X")

# sheety info
project_name = "workoutTracking"
sheet_name = "workouts"
username = os.environ.get("SHEETY_USERNAME")
sheety_endpoint = f"https://api.sheety.co/{username}/{project_name}/{sheet_name}"
header = {
    "Authorization": os.environ.get("SHEETY_AUTHORIZATION"),
}

sheety_params = {
    "workout": {
        "date": today,
        "time": local_time,
        "exercise": workout_name,
        "duration": duration_min,
        "calories": calories_burned,
    }
}

# response = requests.get(url=sheety_endpoint)
response = requests.post(url=sheety_endpoint, json=sheety_params, headers=header)
# response = requests.put(url=f"{sheety_endpoint}/3", json=sheety_params)
# response = requests.delete(url=f"{sheety_endpoint}/3", headers=header)
print(response.text)
