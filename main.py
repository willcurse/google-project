import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 64
HEIGHT_CM = 189
AGE = 23

app_id = "da6b8f2c"
app_key = "83da7abfbbf463e38a32d2b5fbe6d635"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/7c28b56afa1c18b0f1e70f9e48956129/workout/workouts"

exe_text = input("Which exercise you did\n")

header = {
    'x-app-id': app_id,
    'x-app-key': app_key
}

parameter = {
    "query": exe_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameter, headers=header)
result = response.json()

today_date = datetime.now().strftime("%d%m%Y")
today_time = datetime.now().strftime("%X")

# List to store exercises
exercise_list = []

for exercise in result["exercises"]:
    exercise_data = {
        "date": today_date,
        "time": today_time,
        "exercise": exercise["name"].title(),
        "duration": exercise["duration_min"],
        "calories": exercise["nf_calories"],
    }
    exercise_list.append(exercise_data)

# Create JSON data with all exercises
sheet_inputs = {
    "workout": exercise_list
}

sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)


bearer_headers = {
"Authorization": "cbasckbesvbsdfvnl"
}
sheet_response = requests.post(
    sheet_endpoint, 
    json=sheet_inputs, 
    headers=bearer_headers
)