import os
import sys
import requests


API_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city, api_key):
    """Fetch current weather details for a city from OpenWeatherMap."""
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
    }
    response = requests.get(API_URL, params=params, timeout=10)

    if response.status_code == 404:
        raise ValueError("City not found. Check the spelling and try again.")
    if response.status_code == 401:
        raise ValueError("API key is invalid or not active yet. Check your key.")
    response.raise_for_status()

    data = response.json()
    return {
        "city": data["name"],
        "country": data["sys"].get("country", ""),
        "temperature": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "humidity": data["main"]["humidity"],
        "description": data["weather"][0]["description"].capitalize(),
        "wind_speed": data["wind"].get("speed", 0),
    }


def main():
    print("=== Basic Weather App ===")
    api_key = os.getenv("OPENWEATHER_API_KEY")

    if not api_key:
        print("API key not found.")
        print("Set the OPENWEATHER_API_KEY environment variable using the README instructions.")
        sys.exit(1)

    city = input("Enter city name: ").strip()
    if not city:
        print("City name cannot be empty.")
        sys.exit(1)

    try:
        weather = get_weather(city, api_key)
        location = weather["city"]
        if weather["country"]:
            location += f", {weather['country']}"

        print(f"\nWeather for {location}")
        print("-" * 30)
        print(f"Condition: {weather['description']}")
        print(f"Temperature: {weather['temperature']} °C")
        print(f"Feels like: {weather['feels_like']} °C")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Wind speed: {weather['wind_speed']} m/s")
    except ValueError as error:
        print(f"Error: {error}")
    except requests.exceptions.Timeout:
        print("The weather service took too long to respond. Please try again.")
    except requests.exceptions.ConnectionError:
        print("Could not connect. Check your internet connection.")
    except requests.exceptions.HTTPError:
        print("The weather service returned an error. Please try again later.")
    except (KeyError, IndexError, TypeError):
        print("The weather response was unexpected. Please try again.")


if __name__ == "__main__":
    main()
