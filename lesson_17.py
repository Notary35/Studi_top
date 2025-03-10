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
    def __init__(self, name: str, age:int, salary: int, threshold_percent_salary: int = 50) -> None:
        self.name = name
        self._age = age
        self.__salary = salary
        self.__threshold_percent_salary: int = threshold_percent_salary
    
    def set_salary(self, value: int) -> None:
        if type(value) != int:
            raise ValueError('Зарплата должна быть числом')
        if value < 0:
            raise ValueError('Зарплата не может быть меньше 0')
        # Проверим чтобы зарплата не колебалась более чем на 50%
        if abs(self.__salary - value) > self.__salary * self.__threshold_percent_salary / 100:
            raise ValueError(f'Зарплата не может быть изменена больше чем на {self.__threshold_percent_salary}%')
        
        self.__salary = value
        
    def get_salary(self) -> int:
        return self.__salary

manager = Employee('John', 30, 100000)
print(manager.get_salary())
manager.set_salary(120000)
print(manager.get_salary())

