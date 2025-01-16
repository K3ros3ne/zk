import requests

# API klíč pro OpenWeatherMap
api_key = 'a023a3be26e530f37924110734b494b1'

def fetch_weather_data(city):
    """
    Funkce pro získání aktuální teploty města.
    Vrací teplotu v °C zaokrouhlenou na dvě desetinná místa.
    """
    # Sestavíme URL pro API požadavek
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    
    # Posíláme požadavek na API
    response = requests.get(url)
    
    # Kontrola, zda je odpověď v pořádku
    if response.ok:
        data = response.json()  # Načteme JSON data
        temp_kelvin = data['main']['temp']  # Získáme teplotu v Kelvinech
        temp_celsius = temp_kelvin - 273.15  # Převod na °C
        return round(temp_celsius, 2)  # Vracíme teplotu zaokrouhlenou na dvě desetinná místa
    else:
        raise Exception(f"Failed to fetch weather data: {response.status_code}, {response.text}")

# Unit testy
from unittest.mock import patch, MagicMock

def test_fetch_weather_data():
    # Simulovaná odpověď z API
    mock_response = {
        "main": {
            "temp": 293.15  # Teplota v Kelvinech
        }
    }
    with patch("requests.get") as mock_get:
        mock_get.return_value = MagicMock(ok=True, status_code=200, json=MagicMock(return_value=mock_response))
        # Test: Převod 293.15 K na 20.0 °C
        assert fetch_weather_data("Prague") == 20.0

if __name__ == "__main__":
    city = input("Enter city name: ")
    try:
        temperature = fetch_weather_data(city)
        print(f"Current temperature in {city}: {temperature} °C")
    except Exception as e:
        print(f"Error: {e}")
