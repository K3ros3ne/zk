import requests
api_key = 'a023a3be26e530f37924110734b494b1'

def fetch_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        kelvin_temp = data["main"]["temp"]
        celsius_temp = kelvin_temp - 273.15
      
        return round(celsius_temp, 2)
    else:
        return "Error: Unable to fetch data"

from unittest.mock import patch, MagicMock

def test_fetch_weather_data():
    mock_response = {
        "main": {
            "temp": 293.15 
        }
    }
    
    with patch("requests.get") as mock_get:
        mock_get.return_value = MagicMock(ok=True, status_code=200, json=MagicMock(return_value=mock_response))
        
        assert fetch_weather_data("Prague") == 20.0

if __name__ == "__main__":
    city = input("Enter city name: ")
    temperature = fetch_weather_data(city)
    print(f"Current temperature in {city}: {temperature} °C")
