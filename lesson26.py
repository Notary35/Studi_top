"""
Тема: Функции. Аннотации типов. typing. Декораторы. Урок 26.

ПРОСТАЯ АННОТАЦИЯ ТИПОВ

:int - целое число
:float - дробное число
:str - строка
:bool - булево значение
:list - список
:tuple - кортеж
:dict - словарь
:None - пустое значение
:set - множество


Простая аннтоцаия коллекций

:list[int] - список из целых чисел
:list[str] - список из строк
:list[dict] - список из словарей
:set[int] - множество из целых чисел


Расширенная аннотация типов

from typing import List, Dict, Set, Union, Tuple, Optional, Dict, Callable, Iterable, Any, Iterator

Callable - вызываемый объект
Any - любой объект
Iterable - итерируемый объект
Iterator - итератор

Dict[str, list[Union[int, str]]] - словарь с ключами типа str и значениями типа списока, содержащего целые числа или строки
"""
from typing import List, Dict, Set, Union, Tuple, Optional, Callable, Iterable, Any, Iterator


# def decorator_1(func: Callable) -> None:
#     def wrapper():
#         print("До вызова функции")
#         func()
#         print("После вызова функции")

#     return wrapper

# def print_hello():
#     print("Hello")

# def print_goodbye():
#     print("Goodbye")

# print_hello_decorated = decorator_1(print_hello)

# print_goodbye_decorated = decorator_1(print_goodbye)

# print_hello_decorated()
# print_goodbye_decorated()

# def decorator_2(func: Callable[[str], str]) -> Callable[[str], str]:
#     def wrapper(s: str) -> str:
#         print("До вызова функции")
#         result = func(s)
#         print("После вызова функции")
#         return result

#     return wrapper

# def print_hello_2(s: str) -> str:
#     return f"Hello, {s}"

# print_hello_2_decorated = decorator_2(print_hello_2)

# print(print_hello_2_decorated("Иосиф"))

# @decorator_2
# def print_goodbye_2(s: str) -> str:
#     return f"Goodbye, {s}"

# print(print_goodbye_2("Иосиф"))

# def decorator_3(func: Callable[[str], str]) -> Callable[[str], str]:
#     def wrapper(*args, **kwargs):
#         print("Что то делаем ДО вызова функции")
#         result = func(*args, **kwargs)
#         print("Что то делаем ПОСЛЕ вызова функции")
#         return result

#     return wrapper

# @decorator_3
# def print_hello_3(name: str, age: int) -> str:
#     return f"Hello, {name} {age}"

# print(print_hello_3("Иосиф", 30))
# print(print_hello_3(name="Иосиф", age=30))

def check_length(length: int = 10) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapper(name: str):
            if len(name) > length:
                return f"Имя {name} слишком длинное"
            else:
                return func(name)
        
        return wrapper
    return decorator
@check_length()
def say_my_name(name: str) -> str:
    return (f"Меня зовут {name}")

print(say_my_name("Иосиф"))
print(say_my_name("Иосиф Иосифович"))