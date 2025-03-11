import requests
from plyer import notification
# Просто сделаем запрос без функций
# pylint: disable=all

CITY = input('Введите город: ')
API_KEY = "23496c2a58b99648af590ee8a29c5348"
UNITS = "metric"
LANGUAGE = "ru"

# url = fr'https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units={UNITS}&lang={LANGUAGE}'

# response = requests.get(url) # Сделали запрос и получили объект ответа
# print(response.status_code) # Получили статус ответа
# print(response.json()) # Получили объект Python из JSON


# Получим описание и температуру, и ощущается как
# weather_dict = response.json()

class WeatherRequest:
    def __init__(self, api_key: str, units: str = "metric", language: str = "ru"):
        self.api_key = api_key
        self.units = units
        self.language = language
        self.__url: str = None
        self.__response: dict = None
    
        
    def __get_request_url(self, city: str) -> str:
        self.__url = fr'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units={self.units}&lang={self.language}'
        
    def get_weather(self, city: str):
        self.__get_request_url(city)
        response = requests.get(self.__url)
        self.__response = response.json()
        
    def get_clear_weather_data(self, city: str):
        self.get_weather(city)
        result = {}
        result["temp"] = self.__response["main"]["temp"]
        result["feels_like"] = self.__response['main']['feels_like']
        result["description"] = self.__response['weather'][0]['description']
        return result

weather = WeatherRequest()
print(weather.get_clear_weather_data(CITY))


# # Temp
# temp = weather_dict['main']['temp']
# # Ощущается как
# feels_like = weather_dict['main']['feels_like']
# # Описание погоды
# description = weather_dict['weather'][0]['description']

# print(f'Температура: {temp}°C\nОщущается как: {feels_like}°C\nОписание: {description}')

# # Уведомление
# notification.notify(
#     title = f"Погода в {CITY}",
#     message = f"Температура: {temp}°C\nОщущается как: {feels_like}°C\nОписание: {description}",
#     app_name = "Погода",
#     app_icon = None,
#     timeout = 0,
#     toast = True,
# )