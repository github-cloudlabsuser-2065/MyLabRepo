import requests

def get_weather(city):
    api_key = "7f0d568faab065b97d0b960e1693f163"  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # You can change the units to imperial if needed
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        weather_data = response.json()
        # Process the weather data as per your requirements
        # For example, you can extract temperature, humidity, etc.
        temperature = weather_data["main"]["temp"]
        #humidity = weather_data["main"]["humidity"]
        # Return the weather information
        return temperature
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return None

# Example usage
city = "London"  # Replace with the desired city
temperature = get_weather("Stockholm")
# if temperature and humidity:
#    print(f"The temperature in {city} is {temperature}°C with {humidity}% humidity.")