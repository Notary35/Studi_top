"""
Lesson 17
11.05.2025
Инкапсуляция. Приватные атрибуты и методы.
"""


class Car:
    def __init__(self, color: str, mark: str, serial_number: int):
        self.color = color
        self.mark = mark
        self.__serial_number = serial_number
    
    def __str__(self) -> str:
        # return f"Цвет: {self.color}\nМарка: {self.mark}\nСерийный номер: {self.serial_number}"
        return f"Автомобиль: {self.mark}\nСерийный номер: {self.__serial_number}\nЦвет: {self.color}"

# pylint: disable=all

"""
Два уровня сокрытия:
_ - защищенный (protected) - условно нет доступа из вне. Есть доступ у наследников
__ - приватный (private) - сложный доступ из вне. Нет доступа у наследников
"""

car = Car("Желтый", "Audi", 999)
# print(car.__serial_number)
print(car.__dict__)
print()
# print({'color': car.__dict__['color']})
print(car._Car__serial_number)
print()
car._Car__serial_number = 333
print(car)
print()
car._serial_number = 111
print(car.__dict__)
print()