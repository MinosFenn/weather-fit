import requests
import json

with open('clothing_items.json') as f:
    clothing_items = json.load(f)

def get_weather(API_KEY, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()


def calculate_layers(temperature):
    layers = {
        "top_layer_0": False,
        "top_layer_1": False,
        "top_layer_2": False,
        "bottom_layer_0": False,
        "bottom_layer_1": False,
    }
    
    if temperature < -20:
        layers.update({
            "top_layer_0": True,
            "top_layer_1": True,
            "top_layer_2": True,
            "bottom_layer_0": True,
            "bottom_layer_1": True
        })
    elif -20 <= temperature <= -5:
        layers.update({
            "top_layer_0": True,
            "top_layer_1": True,
            "top_layer_2": True,
            "bottom_layer_0": True,
            "bottom_layer_1": True
        })
    elif -5 < temperature <= 7:
        layers.update({
            "top_layer_0": True,
            "top_layer_1": True,
            "top_layer_2": True,
            "bottom_layer_1": True
        })
    elif 7 < temperature <= 23:
        layers.update({
            "top_layer_0": True,
            "top_layer_1": True,
            "bottom_layer_1": True
        })
    elif 23 < temperature <= 35:
        layers.update({
            "top_layer_0": True,
            "bottom_layer_1": True
        })
    else:
        layers.update({
            "top_layer_0": True,
            "bottom_layer_1": True
        })
    
    return layers


def recommend_best_clothing(temperature, layers):
    # Calculate desired clothHeatScore
    desired_score = -temperature + 35
    
    # Determine the required layers based on the temperature    
    recommended_clothing = {
        "top_layer_0": [],
        "top_layer_1": [],
        "top_layer_2": [],
        "bottom_layer_0": [],
        "bottom_layer_1": []
    }
    
    # Check each clothing item and select the best ones based on the closest clothHeatScore
    for item in clothing_items:
        layer_type = item['clothCategory']
        if layers.get(layer_type, True):
            recommended_clothing[layer_type].append(item)
    
    # Sort each layer's list by the closeness of the clothHeatScore to the desired_score
    for layer, items in recommended_clothing.items():
        items.sort(key=lambda x: abs(x['clothHeatScore'] - desired_score))
        recommended_clothing[layer] = items[:1]  # Select the best one for each layer
    
    # Filter out layers that are not needed (remain empty)
    recommended_clothing = {k: v for k, v in recommended_clothing.items() if v}
    
    return recommended_clothing

