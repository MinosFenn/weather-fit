import requests
import json

with open('accessories_items.json') as f:
    accessories_items = json.load(f)

def get_weather(API_KEY, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()


def calculate_accessories(temperature, wind, humidity, weather_condition, weather_description):
    accessories = {
        "top_layer_0": False,
        "top_layer_1": False,
        "top_layer_2": False,
        "bottom_layer_0": False,
        "bottom_layer_1": False,
    }
    
    if temperature < -20:
        accessories.update({
            "top_layer_0": True,
            "top_layer_1": True,
            "top_layer_2": True,
            "bottom_layer_0": True,
            "bottom_layer_1": True
        })
    elif -20 <= temperature <= -5:
        accessories.update({
            "top_layer_0": True,
            "top_layer_1": True,
            "top_layer_2": True,
            "bottom_layer_0": True,
            "bottom_layer_1": True
        })
    elif -5 < temperature <= 7:
        accessories.update({
            "top_layer_0": True,
            "top_layer_1": True,
            "top_layer_2": True,
            "bottom_layer_1": True
        })
    elif 7 < temperature <= 23:
        accessories.update({
            "top_layer_0": True,
            "top_layer_1": True,
            "bottom_layer_1": True
        })
    elif 23 < temperature <= 35:
        accessories.update({
            "top_layer_0": True,
            "bottom_layer_1": True
        })
    else:
        accessories.update({
            "top_layer_0": True,
            "bottom_layer_1": True
        })
    
    return accessories

def recommend_best_accessories(temperature, accessories):
    # Calculate desired clothHeatScore
    desired_score = -temperature + 35
    
    # Determine the required accessories based on the temperature    
    recommended_accessories = {
        "top_layer_0": [],
        "top_layer_1": [],
        "top_layer_2": [],
        "bottom_layer_0": [],
        "bottom_layer_1": []
    }
    
    # Check each clothing item and select the best ones based on the closest clothHeatScore
    for item in accessories_items:
        layer_type = item['clothCategory']
        if accessories.get(layer_type, True):
            recommended_accessories[layer_type].append(item)
    
    # Sort each layer's list by the closeness of the clothHeatScore to the desired_score
    for layer, items in recommended_accessories.items():
        items.sort(key=lambda x: abs(x['clothHeatScore'] - desired_score))
        recommended_accessories[layer] = items[:1]  # Select the best one for each layer
    
    # Filter out accessories that are not needed (remain empty)
    recommended_accessories = {k: v for k, v in recommended_accessories.items() if v}
    
    return recommended_accessories

