import os
import requests
from smart_agri_agent.models.contracts import WeatherAnalysisInput, WeatherAnalysisOutput

def analyze_weather(data: WeatherAnalysisInput) -> WeatherAnalysisOutput:
    """
    Fetches and interprets weather data.
    """
    # For demonstration, we could use a real API like Open-Meteo or OpenWeatherMap.
    # Since we need to geocode the location string, we'll try a public geocoding API.
    # If the network call fails, we raise an explicit error.
    
    # Check if an API key is provided for a paid service, otherwise use free fallback.
    api_key = os.getenv("WEATHER_API_KEY")
    
    try:
        # Geocode the location using Open-Meteo's geocoding API
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={data.location}&count=1&language=en&format=json"
        geo_resp = requests.get(geo_url, timeout=5)
        geo_resp.raise_for_status()
        geo_data = geo_resp.json()
        
        if not geo_data.get("results"):
            raise ValueError(f"Could not find coordinates for location: {data.location}")
            
        lat = geo_data["results"][0]["latitude"]
        lon = geo_data["results"][0]["longitude"]
        
        # Get weather data using Open-Meteo
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_mean,precipitation_probability_mean&hourly=relative_humidity_2m&forecast_days={data.days}"
        weather_resp = requests.get(weather_url, timeout=5)
        weather_resp.raise_for_status()
        weather_data = weather_resp.json()
        
        # Parse results
        daily = weather_data.get("daily", {})
        hourly = weather_data.get("hourly", {})
        
        if not daily or not hourly:
            raise ValueError("Weather API returned malformed data.")
            
        avg_temp = sum(daily.get("temperature_2m_mean", [0])) / max(1, len(daily.get("temperature_2m_mean", [0])))
        rain_chance = sum(daily.get("precipitation_probability_mean", [0])) / max(1, len(daily.get("precipitation_probability_mean", [0])))
        
        # Humidity is hourly, calculate average
        humidities = hourly.get("relative_humidity_2m", [0])
        avg_humidity = sum(humidities) / max(1, len(humidities))
        
        return WeatherAnalysisOutput(
            avg_temp=round(avg_temp, 2),
            humidity=round(avg_humidity, 2),
            rain_chance=round(rain_chance, 2)
        )
        
    except requests.exceptions.RequestException as e:
        # Handle network failures safely without fabricating data
        raise RuntimeError(f"External weather API failed: {str(e)}")
