import requests
api_key = 'a023a3be26e530f37924110734b494b1'

def fetch_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        temp_kelvin = data["main"]["temp"]
        
        temp_celsius = round(temp_kelvin - 273.15, 2)
        
        return temp_celsius
    else:
        print(f"Error: Unable to fetch data for {city}. Status code: {response.status_code}")
        return None

from unittest.mock import patch, MagicMock

def test_fetch_weather_data():
    mock_response = {
        "main": {
            "temp": 293.15  # Teplota v Kelvinech
        }
    }
    with patch("requests.get") as mock_get:
        mock_get.return_value = MagicMock(ok=True, status_code=200, json=MagicMock(return_value=mock_response))
        assert fetch_weather_data("Prague") == 20.0  # 293.15 K = 20.0 °C

if name == "main":
    city = input("Enter city name: ")
    temperature = fetch_weather_data(city)
    if temperature is not None:
        print(f"Current temperature in {city}: {temperature} °C")
