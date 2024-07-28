from flask import Blueprint, request, jsonify, current_app
from .weather import get_weather, recommend_clothing

bp = Blueprint('routes', __name__)

@bp.route('/recommend', methods=['GET'])
def recommend():
    api_key = current_app.config['API_KEY']
    location = current_app.config['LOCATION']

    weather_data = get_weather(api_key, location)
    temperature = weather_data['main']['temp']
    name = weather_data['name']
    weather_condition = weather_data['weather'][0]['main']

    recommendations = recommend_clothing(temperature, weather_condition)
    print(f"Current temperature in {name}: {temperature}°C")
    return jsonify(recommendations)
