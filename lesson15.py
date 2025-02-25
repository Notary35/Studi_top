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

