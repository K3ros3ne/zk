import requests

# API ключ для OpenWeatherMap
api_key = 'a023a3be26e530f37924110734b494b1'

def fetch_weather_data(city):
    """
    Получение текущей температуры для заданного города.
    Возвращает температуру в градусах Цельсия или "N/A" при ошибке.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    
    try:
        response = requests.get(url)
        if response.ok:
            data = response.json()
            temp_kelvin = data['main']['temp']
            temp_celsius = temp_kelvin - 273.15
            return round(temp_celsius, 2)
        else:
            # Если ответ от сервера содержит ошибку, возвращаем "N/A"
            return "N/A"
    except requests.exceptions.RequestException:
        # Если есть проблемы с сетью или сервером, возвращаем "N/A"
        return "N/A"

if __name__ == "__main__":
    city = input("Enter city name: ").strip()
    if city:
        temperature = fetch_weather_data(city)
        # Выводим температуру или "N/A"
        print(f"Current temperature in {city}: {temperature} °C")
    else:
        print("City name cannot be empty.")
