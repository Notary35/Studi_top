import requests
import telebot

API_KEY = "23496c2a58b99648af590ee8a29c5348"


class WeatherAPI:
    def __init__(self, api_key: str, telegram_token: str):
        self.api_key = api_key
        self.bot = telebot.TeleBot(telegram_token)

    def get_weather(self, city: str) -> dict:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric&lang=ru"
        response = requests.get(url, timeout=5).json()
        return {
            "temp": response["main"]["temp"],
            "feels_like": response["main"]["feels_like"],
            "description": response["weather"][0]["description"],
        }

    def send_telegram(self, chat_id: str, city: str):
        try:
            weather = self.get_weather(city)
            message = f'Погода в городе {city}:\nТемпература: {weather["temp"]}°C\nОщущается как: {weather["feels_like"]}°C\nОписание: {weather["description"]}'
            # Преобразуем chat_id в целое число, так как Telegram принимает только числовой формат
            self.bot.send_message(int(chat_id), message)
            print(f"Погода отправлена в Telegram")

        except Exception as e:
            print(f"Ошибка: {e}")


if __name__ == "__main__":
    API_KEY = "23496c2a58b99648af590ee8a29c5348"
    TELEGRAM_TOKEN = "8122692273:AAH-TLwdFymR78NXkL-GqlbcZT8m4wIC7MU"

    weather = WeatherAPI(API_KEY, TELEGRAM_TOKEN)

    while True:
        city = input("Введите название города (или 'стоп' для выхода): ")
        if city.lower() == "стоп":
            print("Программа завершена!")
            break

        chat_id = input("Введите chat_id получателя в Telegram: ")
        while not chat_id.strip():  # Проверяем на пустой ввод
            print("Chat ID не может быть пустым!")
            chat_id = input("Введите chat_id получателя в Telegram: ")

        weather.send_telegram(chat_id, city)
# 788722299