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

# Создаём атрибуты класса Car
# Это разные объекты, они имеют разные адреса в ОЗУ
car_1 = Car()
car_2 = Car()

print(car_1)
print()
print(type(car_1.mark))
print()
print(car_2)
print()

# У нас есть доступ к атрибутам класса через объект. Название атрибута
print(f'Это автомобиль {car_1.mark} цветом {car_1.color}') # Это автомобиль BMW цветом Black
print()
print(car_2.color) # Black
print()

# Мы можем переопределить атрибуты если нужно
car_2.color = "Red"
car_2.options = ["ABS"] # добавляем новый атрибут вне класса, работать будет но не рекомендуется
print(car_2.color) # Red
print()
print(car_2.options) # ['ABS']
print()
print(car_1.color) # Black