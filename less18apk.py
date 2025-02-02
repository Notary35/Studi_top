import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

API_KEY = "23496c2a58b99648af590ee8a29c5348"

class WeatherAPI:
    def __init__(self, api_key: str, email_from: str, email_password: str):
        self.api_key = api_key
        self.email_from = email_from
        self.email_password = email_password
        
    def get_weather(self, city: str) -> dict:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric&lang=ru'
        response = requests.get(url, timeout=5).json()
        return {
            "temp": response["main"]["temp"],
            "feels_like": response["main"]["feels_like"],
            "description": response["weather"][0]["description"]
        }

    def send_email(self, email_to: str, city: str):
        try:
            weather = self.get_weather(city)
            message = f'Температура: {weather["temp"]}°C\nОщущается как: {weather["feels_like"]}°C\nОписание: {weather["description"]}'
            
            msg = MIMEMultipart()
            msg['From'] = self.email_from
            msg['To'] = email_to
            msg['Subject'] = f"Погода в городе {city}"
            msg.attach(MIMEText(message, 'plain'))

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(self.email_from, self.email_password)
            server.send_message(msg)
            server.quit()
            
            print(f"Погода отправлена на {email_to}")
            
        except Exception as e:
            print(f"Ошибка: {e}")

class WeatherApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.city_input = TextInput(hint_text='Введите город')
        self.email_input = TextInput(hint_text='Введите email')
        self.result_label = Label(text='')
        
        button = Button(text='Получить погоду')
        button.bind(on_press=self.get_weather)
        
        layout.add_widget(self.city_input)
        layout.add_widget(self.email_input)
        layout.add_widget(button)
        layout.add_widget(self.result_label)
        
        return layout

    def get_weather(self, instance):
        # Здесь код получения погоды
        pass

if __name__ == '__main__':
    WeatherApp().run()