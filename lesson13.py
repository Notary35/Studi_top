"""
Урок 13
15.12.2024

python функции. **kwargs. Модули. Библиотеки plyer и requests. Урок: 13

1. Разбор **kwargs - "распаковка" словаря

2. Работа с внешними библиотеками:
    - Установка через pip
    - Импорт модулей
    - Библиотека plyer для уведомлений
    - Библиотека requests для HTTP запросов

3. Создание модулей:
    - Разделение кода на модули
    - Импорт собственных модулей
    - Относительные и абсолютные импорты
    - __name__ == '__main__'

4. Практика:
    - Создание функций для работы с API
    - Отправка уведомлений через plyer
    - Получение данных через requests
    - Структурирование кода в модули
"""

# Kwargs

# Простой пример разбора словаря:

# Создаем словарь с данными пользователя, где 'name' и 'age' - ключи, а 'Иван' и 25 - значения
user = {"name": "Иван", "age": 25}

# Используем метод values() для получения значений и распаковываем их в переменные name и age
name, age = user.values()

# Выводим результат через f-строку, где переменные подставляются в фигурных скобках
print(f"Имя: {name}, возраст: {age}")

# Пример посложенее - распаковка вложенных словарей
student = {"info": {"name": "Мария", "age": 20}, "grades": {"math": 5, "physics": 4}}

info, grades = student.values()
print(f"Информация:  {info}")
print(f"Оценки: {grades}")

# Распаковка с использованием **kwargs
default = {"name": "Ваня", "age": 25}
custom = {"full_name": "Иван", "Birthday": "15.01.2000"}
config = {*default, *custom}
print(f"Итоговая конфигурация: {config}")

# Как это было бы через Update
new_dict = {}
new_dict.update(default)
new_dict.update(custom)
print(f"Итоговая конфигурация: {new_dict}")

# Создадим функцию для **kwargs:


# 1:
def print_user_info(**kwargs):
    print(type(kwargs))  # <class 'dict'>
    for key, value in kwargs.items():
        print(f"Ключ: {key}, Значение: {value}")


print_user_info(name="Иван", age=25)

# 2:
user_info = {"name": "Эрик", "age": 30, "city": "Лиссабон"}
print_user_info(**user_info)
print_user_info(hobbies=["чтение", "путешествия", "программирование"])

сonfig_open_ai = {
    "model": "gpt-3.5-turbo",
    "temperature": 0.7,
    "max_tokens": 50,
    "top_p": 1.0,
    "frequency_penalty": 0.0,
    "presence_penalty": 0.0,
    "api_key": "sk-...",
    "endpoint": "https://api.openai.com/v1/chat/completions",
}


def open_ai_request(**params):
    # Тут вы можете разобрать словарь и добыть нужное
    pass


def open_ai_request2(
    model: str,
    temperature: float,
    max_tokens: int,
    top_p: float,
    frequency_penalty: float,
    presence_penalty: float,
    api_key: str,
    endpoint: str,
):
    # Этот вариант лучше, т.к. он более читаемый и удобный
    pass


open_ai_request2(**сonfig_open_ai)

open_ai_request2(
    model="gpt-3.5-turbo",
    temperature=0.7,
    max_tokens=50,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    api_key="sk-...",
    endpoint="https://api.openai.com/v1/chat/completions",
)

user_info = {"name": "Эрик", "age": 30, "city": "Лиссабон"}


def print_user_info2(name, age, city):
    print(f"Имя: {name}, Возраст: {age}, Город: {city}")


print_user_info2(**user_info)

config = {"sep": " ", "end": "\n"}

print("Hello", "World", **config)

