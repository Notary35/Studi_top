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
        """
        Метод
        :param: city: Название города
        :return: None
        """
        self.__url = fr'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units={self.units}&lang={self.language}'
        
    def get_weather(self, city: str):
        """
        Метод формирует URL и делает запрос к погодному API
        :param city: Название города
        :return: None
        """
        self.__get_request_url(city)
        response = requests.get(self.__url)
        self.__response = response.json()
        
    def get_clear_weather_data(self, city: str):
        """
        Метод очищает данные полученные из погодного API и упаковывает их в словарь,
        с 3мя ключами. Температура, ощущается как и описание погоды.
        :param city: Название города
        :return: Словарь с очищенными данными
        """
        self.get_weather(city)
        result = {}
        result["temp"] = self.__response["main"]["temp"]
        result["feels_like"] = self.__response['main']['feels_like']
        result["description"] = self.__response['weather'][0]['description']
        
        return result
    
    def get_weather_string(self, weather_dict: dict) -> str:
        """
        Метод возвращает строку с описанием погоды
        :param weather_dict: Словарь с данными о погоде
        :return: Строка с описанием погоды
        """
        temp = weather_dict["temp"]
        feels_like = weather_dict["feels_like"]
        description = weather_dict["description"]
        return f"Температура: {temp}°C\nОщущается как: {feels_like}°C\nОписание: {description}"
    
    def __call__ (self, city: str) -> str:
        weather_data = self.get_clear_weather_data(city)
        return self.get_weather_string(weather_data)
    
    def weather_notify(self, city: str):
        weather_data = self.get_clear_weather_data(city)
        notification.notify(
            title = f"Погода в {city}",
            message = f"Температура: {weather_data['temp']}°C\nОщущается как: {weather_data['feels_like']}°C\nОписание: {weather_data['description']}",
            app_name = "Погода",
            app_icon = None,
            timeout = 0,
            toast = True,
        )

weather = WeatherRequest(API_KEY)
result = weather(CITY)
print(result)
weather.weather_notify(CITY)


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