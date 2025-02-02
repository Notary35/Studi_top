import requests
import subprocess

class WeatherAPI:
    def __init__(self, api_key: str):
        self.api_key = api_key
        
    def get_weather(self, city: str) -> dict:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric&lang=ru'
        response = requests.get(url, timeout=5).json()
        return {
            "temp": response["main"]["temp"],
            "description": response["weather"][0]["description"]
        }

    def send_sms(self, phone: str, city: str):
        try:
            weather = self.get_weather(city)
            message = f'Погода в {city}: {weather["temp"]}°C, {weather["description"]}'
            
            adb_command = f'adb shell am start -a android.intent.action.SENDTO -d sms:{phone} --es sms_body "{message}"'
            subprocess.run(adb_command, shell=True)
            
            print(f"SMS подготовлено для отправки на номер {phone}")
            
        except Exception as e:
            print(f"Ошибка: {e}")

if __name__ == '__main__':
    API_KEY = "23496c2a58b99648af590ee8a29c5348"
    weather = WeatherAPI(API_KEY)
    
    while True:
        city = input("Введите название города (или 'стоп' для выхода): ")
        if city.lower() == 'стоп':
            print("Программа завершена!")
            break
        phone = input("Введите номер телефона получателя: ")
        weather.send_sms(phone, city)