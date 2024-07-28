import requests
import json

with open('clothing_items.json') as f:
    clothing_items = json.load(f)

def get_weather(API_KEY, location):
    print(location)
    print(API_KEY)
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
    print(url)
    response = requests.get(url)
    print(response.json())

    return response.json()

def recommend_clothing(temperature, weather_condition):
    recommended_items = []
    for item in clothing_items:
        if temperature <= 10 and item["clotheHeatScore"] >= 7:
            recommended_items.append(item)
        elif 10 < temperature <= 20 and item["clotheHeatScore"] >= 4 and item["clotheHeatScore"] <= 6:
            recommended_items.append(item)
        elif temperature > 20 and item["clotheHeatScore"] <= 3:
            recommended_items.append(item)
        # Add more conditions based on weather_condition (e.g., rain, wind)
    return recommended_items

