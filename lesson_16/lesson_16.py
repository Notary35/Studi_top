"""
Lesson 16
29.12.2024

Python: ООП. Ч1. Нейминг. Атрибуты. Методы. Урок: 16
- Нейминг
"""

"""
UpperCamelCase - первое слово с большой буквы, остальные с маленькой. Каждое новое слово с большой буквы.

Название должно быть информативным. Передаввать смысл. Как правило это существительные или прилагательные.
"""

class User:
    pass # заглушка

name = __name__
print(name) # __main__
print()
user = User()
print(user) # <__main__.User object at 0x0000020C2F68F190>
print()
print(type(user)) # <class '__main__.User'>
print()

srting_1 = str("Строка_1")
srting_2 = str("Строка_2")
srting_3 = str("Строка_3")
print(type(srting_1)) # <class 'str'>
print()
print(srting_1)
print()

class Car:
    mark: str = "BMW"
    color: str = "Black"

car_1 = Car()
car_2 = Car()
car_3 = Car()

car_2.color = "Red"

Car.color = "Blue"

print(car_1.color) # Blue
print(car_2.color) # Red
print(car_3.color) # Blue

# Атрибуты класса и атрибуты экземпляра класса

"""
Атрибуты класса - это атрибуты которые принадлежат классу.
Эти данные общие для всех экземпляров класса.
И их можно изменить глобально для всех экземпляров.

Атрибуты экземпляра класса - это атрибуты которые принадлежат конкретному экземпляру класса.
Эти данные уникальные для каждого экземпляра класса.
"""