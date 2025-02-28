"""
lesson №15 (25.02.2025)

Python: Работа с форматами данных JSON, CSV, YAML. Урок: 15

1. Формат JSON:
    - Структура и синтаксис JSON
    - Методы json.dumps() и json.loads()
    - Работа с json.dump() и json.load()
    - Обработка сложных структур данных

2. Формат CSV:
    - Структура CSV формата
    - Модуль csv
    - Чтение CSV через csv.reader()
    - Запись CSV через csv.writer()
    - Работа с csv.DictWriter() и csv.DictReader()

3. Формат YAML:
    - Особенности синтаксиса YAML
    - Утсновка библиотеки PyYAML
    - Методы yaml.dump() и yaml.safe_load()
    - Конвертация между форматами

4. Практическое применение:
    - Сохранение конфигураций приложения
    - Работа с табличными данными
    - Парсинг внешних источников данных
    - Конвертация между форматами

Практика:
    - Создание конфигурационного файла в YAML
    - Обработка данных из CSV-файла
    - Сериализация объектов в JSON
    - Конвертер данных между форматами
"""

# JSON - (JavaScript Object Notation)
# JSON - это текстовый формат данных, который используется для представления структурных данных.
# JSON поддерживает следующие типы данных:
# - числа
# - строки
# - логические значения (true, false)
# - массивы
# - объекты
# - null

# Python имеет встроенный модуль json, который позволяет работать с JSON-данными.
# Модуль json предоставляет следующие функции:
# - json.dumps() - конвертирует объект Python в строку JSON
# - json.loads() - конвертирует строку JSON в объект Python
# - json.dump() - записывает объект Python в файл JSON
# - json.load() - читает объект Python из файла JSON


import json
import csv
import pprint


# json_string = """[
#     "Монин Владимир Александрович",
#     "Артемьев Алексей Львович",
#     "Багаутдинов Ринат Дмиитриевич",
#     "Балагуров Артем Алексеевич",
#     "Бибиков Кирилл Сергеевич",
#     "Крылов Илья Сергеевич",
#     "Кряжев Руслан Анатольевич",
#     "Кузнецов Иван Станиславович",
#     "Лапицкая Наталья Владимировна",
#     "Морозов Илья Иванович",
#     "Мустяцэ Иван Иванович",
#     "Никулина Екатерина Александровна"
# ]
# """


# python_data = json.loads(json_string)
# print(type(python_data))
# pprint.pprint(python_data, indent=4)

# Обратная операция
# json_string = json.dumps(python_data, ensure_ascii=False, indent=4)
# print(type(json_string))
# print(json_string)


# Запись в файл
# students.json - файл
# w - режим записи
# encoding="utf-8" - кодировка
# as file - переменная, которая будет содержать файл
# json.dump - метод для записи в файл
# ensure_ascii=False - не конвертировать в ASCII *при работе с русским языком
# with open("students.json", "w", encoding="utf-8") as file:
#     json.dump(python_data, file, ensure_ascii=False, indent=4)

# Чтение из файла
# r - режим чтения
# encoding="utf-8" - кодировка

# with open("students.json", "r", encoding="utf-8") as file:
#     python_data = json.load(file)


# print(type(python_data))
# pprint.pprint(python_data, indent=4)

# Дозапись в файл
# Использование флага "a" для дозаписи в JSON массивах не поддерживается, т.к. он не умеет дозаписывать в конец, а создает новый массив тем самым нарушает структуру данных JSON.
# Заместо этого мы разберём весь массив и дозапишем его в новый обновленный массив.

# Для этого прочитаем файл, добавим новый элемент и запишем обратно в файл:

# with open("students.json", "r", encoding="utf-8") as file:
#     python_data = json.load(file)

# if "Папилов Сергей Вадимович" not in python_data:
#     python_data.append("Папилов Сергей Вадимович")
#     # python_data.remove("Папилов Сергей Вадимович") - удаление элемента

# with open("students.json", "w", encoding="utf-8") as file:
#     json.dump(python_data, file, ensure_ascii=False, indent=4)

# print(type(python_data))
# print(json.dumps(python_data, ensure_ascii=False, indent=4))


def append_json(
    file_name: str, *data: str, indent: int = 4, encoding: str = "utf-8"
) -> None:

    #     """
    #     Функция для добавления данных в JSON-файл. Работает с JSON массивами.
    #     :param file_name: имя JSON-файла
    #     :param data: данные, которые нужно добавить в массив
    #     :param indent: количество пробелов для отступа
    #     :param encoding: кодировка файла
    #     :return: None
    #     """
    with open(file_name, "r", encoding="utf-8") as file:
        python_data = json.load(file)

    if not isinstance(python_data, list):
        raise TypeError("JSON-файл должен содержать список")

    python_data.extend(data)

    with open(file_name, "w", encoding=encoding) as file:
        json.dump(python_data, file, ensure_ascii=False, indent=indent)

    print(isinstance(python_data, list))


# Читаем текущий список из JSON
with open("students.json", "r", encoding="utf-8") as file:
    current_students = json.load(file)

user_input = input("Введите список студентов через запятую: ")

if user_input:
    new_students = user_input.strip().title().split(", ")
else:
    new_students = (
        []
    )  # Данная запись проверяет, что список user_input не пустой (всё равно что if len(user_input > 0) или if user_input != []):

# Преобразуем списки во множества и находим разницу, функцией "list" преобразуем обратно в список
students_to_add = list(set(new_students) - set(current_students))

append_json("students.json", *students_to_add)

with open("students.json", "r", encoding="utf-8") as file:
    current_students = json.load(file)


print(type(current_students))
print(json.dumps(current_students, ensure_ascii=False, indent=4))




def remove_json(file_name: str, *data: str, indent: int = 4, encoding: str = "utf-8") -> None:
    with open(file_name, "r", encoding="utf-8") as file:
        python_data = json.load(file)

    if not isinstance(python_data, list):
        raise TypeError("JSON-файл должен содержать список")

    # Оставляем только те элементы, которых нет в data
    python_data = list(set(python_data) - set(data))

    # Сортируем список по фамилии (первое слово в строке)
    python_data.sort(key=lambda x: x.split(" ")[0])

    with open(file_name, "w", encoding=encoding) as file:
        json.dump(python_data, file, ensure_ascii=False, indent=indent)

# Чтение текущего списка
with open("students.json", "r", encoding="utf-8") as file:
    current_students = json.load(file)

user_input = input("Введите список студентов, которых нужно удалить, через запятую: ")

if user_input:
    students_to_remove = user_input.strip().title().split(", ")
else:
    students_to_remove = []

remove_json("students.json", *students_to_remove)# print(json.dumps(current_students, ensure_ascii=False, indent=4))

with open("students.json", "r", encoding="utf-8") as file:
    current_students = json.load(file)

print(type(current_students))
pprint.pprint(current_students, indent=4)