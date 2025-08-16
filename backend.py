from dotenv import load_dotenv
import requests
import os

load_dotenv()

def get_data(place, days, kind):
    API_KEY = os.getenv("API_KEY")
    URL = (f"http://api.openweathermap.org/data/2.5/forecast?"
           f"q={place}&"
           f"appid={API_KEY}")
    request = requests.get(URL)
    content = request.json()
    filtered_data = content["list"]
    nr_values = days * 8
    filtered_data = filtered_data[:nr_values]
    if kind == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if kind == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data


if __name__ == "__main__":
    print(get_data("Karachi", 1, "Temperature"))
    print(get_data("Karachi", 1, "Sky"))