"""
Lesson 16
29.12.2024

Python: ООП. Ч1. Нейминг. Атрибуты. Методы. Урок: 16
- Нейминг.
- Атрибуты класса
- Инициализатор
- Self
- __str__ 
- Методы экземпляра
"""

"""
UpperCamelCase - первое слово с большой буквы, остальные с маленькой. Каждое новое слово с большой буквы.

Название должно быть информативным. Передаввать смысл. Как правило это существительные или прилагательные.
"""
# __name__ - имя модуля. Если мы запускаем файл напрямую, то __name__ = __main__. Если мы импортируем, то __name__ = имя модуля.

# __init__ - инициализатор класса. Вызывается при создании экземпляра класса атрибутами и методами.


class Car:
    def __init__(self, model: str, color: str, year: int):
        self.model = model
        self.color = color
        self.year = year
        print(f'Модель: {self.model}\nЦвет: {self.color}\nГод выпуска: {self.year}\n')
    
    
    def __str__(self) -> str:
        return f"Модель: {self.model}\nЦвет: {self.color}\nГод выпуска: {self.year}"
        

    def make_beep(self, count: int) -> str:
        return f'Автомобиль {self.model} сделал {"Beep " * count}'
    
    @staticmethod # статический метод. Не принимает ни self, ни cls. Может вызываться без создания экземпляра класса.
    def get_auto_value(width: int, height: int, depth: int) -> int:
        return width * height * depth

car_1 = Car('BMW', 'red', 2020)
car_2 = Car('Mercedes', 'black', 2021)
