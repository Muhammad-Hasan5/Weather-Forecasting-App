from dotenv import load_dotenv
import requests
import os

load_dotenv()

def get_data(place, days):
    API_KEY = os.getenv("API_KEY")
    URL = (f"http://api.openweathermap.org/data/2.5/forecast?"
           f"q={place}&"
           f"appid={API_KEY}")
    request = requests.get(URL)
    content = request.json()
    filtered_data = content["list"]
    nr_values = days * 8
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__ == "__main__":
    get_data(place="karachi", days=3)