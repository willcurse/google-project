import requests

GENDER = "male"
WEIGHT_KG = 64
HEIGHT_CM = 189
AGE = 23

APP_ID = "da6b8f2c"
API_KEY = "83da7abfbbf463e38a32d2b5fbe6d635"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)
