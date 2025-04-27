from dotenv import load_dotenv
import requests
import os

load_dotenv()


def get_weather() -> None:
    url = "https://api.weatherapi.com/v1/current.json"
    api_key = os.getenv("API_KEY")
    city = "Paris"
    response_json = requests.get(f"{url}?key={api_key}&q={city}").json()
    print(f"Celsius: {response_json['current']['temp_c']}")
    print(f"Fahrenheit: {response_json['current']['temp_f']}")


if __name__ == "__main__":
    get_weather()
