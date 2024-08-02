from flask import Blueprint, request, jsonify, current_app
from .weather import get_weather, calculate_layers, recommend_best_clothing

bp = Blueprint('routes', __name__)

@bp.route('/recommend', methods=['GET'])
def recommend():
    api_key = current_app.config['API_KEY']
    location = current_app.config['LOCATION']
    
    weather_data = get_weather(api_key, location)

    location_name = weather_data['name']
    weather_condition = weather_data['weather'][0]['main']
    weather_description = weather_data['weather'][0]['description']

    temperature_feel = weather_data['main']['feels_like']
    temp_min = weather_data['main']['temp_min']
    temp_max = weather_data['main']['temp_max']    
    humidity = weather_data['main']['humidity']
    wind = weather_data['wind']['speed']



    # recommendations = recommend_clothing(temperature_feel, weather_condition)
    print(f"Current temperature in {location_name}: {temperature_feel}°C, min:{temp_min} ,max:{temp_max} ,wind:{wind} ,humidity:{humidity}" )
    layers = calculate_layers(temperature_feel)
    print("Recommended layers:", layers)
    best_clothing = recommend_best_clothing(temperature_feel, layers)
    print("Recommended clothing:", best_clothing)
    return best_clothing
        
