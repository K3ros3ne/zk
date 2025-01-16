import requests
api_key = 'a023a3be26e530f37924110734b494b1'

def fetch_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    
    try:
        response = requests.get(url)
        if response.ok:
            data = response.json()
            temp_kelvin = data['main']['temp']
            temp_celsius = temp_kelvin - 273.15
            return round(temp_celsius, 2)
        else:
            return "error"
    except requests.exceptions.RequestException:

if __name__ == "__main__":
    city = input("Enter city name: ")
    if city:
        temperature = fetch_weather_data(city)
        print(f"Current temperature in {city}: {temperature} °C")
    else:
        print("City name cannot be empty.")
