"""
Lesson 17
11.05.2025
Инкапсуляция. Приватные атрибуты и методы.
- Приватные атрибуты
- Приватные методы
- Защищенные атрибуты
- Защищенные методы
- Доступы из вне
"""
# pylint: disable=all
class Employee:
    def __init__(self, name: str, age:int, salary: int) -> None:
        self.name = name
        self._age = age
        self.__salary = salary
        
    def get_salary(self) -> int:
        return self.__salary
    
    def set_salary(self, value: int) -> None:
        self.__salary = value