"""
Lesson 17
11.05.2025
Инкапсуляция. Приватные атрибуты и методы.
- Приватные атрибуты
- Приватные методы
- Защищенные атрибуты
- Защищенные методы
- Доступы из вне

Делаем 2 метода, которые называются одинаково
Например это salary

@property
def salary - это для добычи данных из приватных атрибутов

@salary.setter - мы делаем сеттер для конкретного атрибута
"""

class SalaryException(ValueError):
    """
    Ошибка связанна с изменением в ЗП
    """
    pass
# pylint: disable=all
class Employee:
    def __init__(self, name: str, age:int, salary: int, threshold_percent_salary: int = 50) -> None:
        self.name = name
        self._age = age
        self.__salary = salary
        self.__threshold_percent_salary: int = threshold_percent_salary
    
    @property
    def salary(self) -> int:
        return self.__salary
    
    @salary.setter
    def salary(self, value: int) -> None:
        if type(value) != int:
            raise SalaryException('Зарплата должна быть числом')
        if value < 0:
            raise SalaryException('Зарплата не может быть меньше 0')
        # Проверим чтобы зарплата не колебалась более чем на 50%
        if abs(self.__salary - value) > self.__salary * self.__threshold_percent_salary / 100:
            raise SalaryException(f'Зарплата не может быть изменена больше чем на {self.__threshold_percent_salary}%')
        
        self.__salary = value

manager = Employee('John', 30, 100000)
print(manager.salary)

while True:
    new_salary = int(input('Введите новую зарплату: '))
    try:
        manager.salary = new_salary
    except SalaryException as e:
        print(e)
    else:
        print(f'Новая зарплата: {manager.salary}')
        break
