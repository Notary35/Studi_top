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

import csv
import pprint

# CSV (Comma-Separated Values)
# CSV - это текстовый формат данных, который используется для представления табличных данных.


students_list = [
    ["lastname", "firstname", "middlename"],
    ["Монин", "Владимир", "Александрович"],
    ["Артемьев", "Алексей", "Львович"],
    ["Багаутдинов", "Ринат", "Дмитриевич"],
    ["Балагуров", "Артем", "Алексеевич"],
    ["Бибиков", "Кирилл", "Сергеевич"],
    ["Крылов", "Илья", "Сергеевич"],
    ["Кряжев", "Руслан", "Анатольевич"],
    ["Кузнецов", "Иван", "Станиславович"],
    ["Лапицкая", "Наталья", "Владимировна"],
    ["Мазуренко", "Кристина", "Владимировна"],
    ["Морозов", "Илья", "Валерьевич"],
    ["Мустяцэ", "Иван", "Иванович"],
    ["Никулина", "Екатерина", "Александровна"],
]

# with open('lesson15.csv', 'w', encoding='utf-8-sig') as file:
#     writer = csv.writer(file, delimiter=';', lineterminator='\n')
#     writer.writerows(students_list)

# writerows() - записывает список списков в файл
# writerow - записывает строку
# utf-8-sig - кодировка для excel
# delimiter=';' - разделитель полей (Для Excel)
# lineterminator='\n' - символ переноса строки

# Дозапись в CSV

new_student = ["Папилов", "Сергей", "Вадимович"]

# students_list.append(new_student)

with open("lesson15.csv", "a", encoding="utf-8-sig") as file:
    writer = csv.writer(file, delimiter=";", lineterminator="\n")
    writer.writerow(new_student)

# Получим данные из CSV обратно

with open("lesson15.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.reader(file, delimiter=";")
    students_list = list(reader)

pprint.pprint(students_list, indent=4)

# with open('lesson15.csv', 'a', encoding='utf-8-sig') as file:
#     writer = csv.DictWriter(file, fieldnames=['Папилов', 'Сергей', 'Вадимович'], delimiter=';')
#     writer.writerows(students_list)

students_dict = [
    {"lastname": "Монин", "firstname": "Владимир", "middlename": "Александрович"},
    {"lastname": "Артемьев", "firstname": "Алексей", "middlename": "Львович"},
    {"lastname": "Багаутдинов", "firstname": "Ринат", "middlename": "Дмитриевич"},
    {"lastname": "Балагуров", "firstname": "Артем", "middlename": "Алексеевич"},
    {"lastname": "Бибиков", "firstname": "Кирилл", "middlename": "Сергеевич"},
    {"lastname": "Крылов", "firstname": "Илья", "middlename": "Сергеевич"},
    {"lastname": "Кряжев", "firstname": "Руслан", "middlename": "Анатольевич"},
    {"lastname": "Кузнецов", "firstname": "Иван", "middlename": "Станиславович"},
    {"lastname": "Лапицкая", "firstname": "Наталья", "middlename": "Владимировна"},
    {"lastname": "Мазуренко", "firstname": "Кристина", "middlename": "Владимировна"},
    {"lastname": "Морозов", "firstname": "Илья", "middlename": "Валерьевич"},
    {"lastname": "Мустяцэ", "firstname": "Иван", "middlename": "Иванович"},
    {"lastname": "Никулина", "firstname": "Екатерина", "middlename": "Александровна"},
]

pprint.pprint(students_dict, indent=4, width=120, sort_dicts=False)


# Запись списка словарей в CSV
# fieldnames - названия для столбцов
# .writeheader() - записывает заголовки

# with open("students.csv", "w", encoding="utf-8-sig") as file:
#     writer = csv.DictWriter(
#         file, fieldnames=students_dict[0].keys(), delimiter=";", lineterminator="\n"
#     )
#     writer.writeheader()
#     writer.writerows(students_dict)

new_student = {"lastname": "Папилов", "firstname": "Сергей", "middlename": "Вадимович"}

# Код дозаписи
with open("students.csv", "a", encoding="utf-8-sig") as file:
    writer = csv.DictWriter(
        file, fieldnames=new_student.keys(), delimiter=";", lineterminator="\n"
    )
    writer.writerow(new_student)

# Прочитаем обратно

with open("students.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file, delimiter=";")
    students_dict = list(reader)

pprint.pprint(students_dict, indent=4, width=120, sort_dicts=False)

# pip install tabulate

from tabulate import tabulate

# Отобразим список словарей в виде таблицы

print(tabulate(students_dict, headers="keys", tablefmt="fancy_grid"))

print(tabulate(students_dict, headers="firstrow", tablefmt="grid"))

# Сначала получаем HTML таблицу из tabulate
html_table = tabulate(students_dict, headers="keys", tablefmt="html")

# Модифицируем таблицу, добавляя нужные классы Bootstrap 5
# Заменяем стандартный тег table на table с классами BS5
styled_table = html_table.replace(
    '<table>', 
    '<table class="table table-striped table-hover">'
)

html_template = f"""
<!doctype html>
<html lang="ru">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Список студентов</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
        <div class="container mt-5">
            <h1 class="mb-4">Список студентов</h1>
            {styled_table}
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
    </body>
</html>
"""

with open("students.html", "w", encoding="utf-8") as file:
    file.write(html_template)

# pip install pyYAML

import yaml

# Простой конфиг с базовыми настройками
config = {
    'app_name': 'Мое приложение',
    'version': '1.0',
    'admin': 'Василий Уткин',
    'settings': {
        'theme': 'dark',
        'language': 'ru',
        'notifications': True
    },
    'users': [
        'admin',
        'moderator',
        'guest'
    ]
}

# Записываем в YAML
with open('simple_config.yaml', 'w', encoding='utf-8') as file:
    yaml.dump(config, file, default_flow_style=False, allow_unicode=True)

# Читаем из YAML
with open('simple_config.yaml', 'r', encoding='utf-8') as file:
    loaded_config = yaml.safe_load(file)

print("Наш загруженный конфиг:")
print(loaded_config)