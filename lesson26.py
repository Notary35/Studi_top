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

list_num = [1, 2, 3, 4, 5]

def func(num: List[int]) -> None:
    print(num)

func(list_num)

class MyClass:
    pass

cl: MyClass = MyClass()

def alpha_func(a: Callable[[List[int]], None]) -> None:
    pass
alpha_func(func)


def fucn8(a):
    # a - хранится тут
    def inner8():
        # a - используется тут
        print(a)
    return inner8

banan = print
banan("Привет!")

# Вызов функции 8
foo = fucn8("пирожок")
foo()

def counter(start_value: int) -> Callable[[], int]:
    def step() -> int:
        nonlocal start_value
        start_value += 1
        return start_value
    return step

# Создаём пару счетчиков с разными начальными значениями

counter1 = counter(10)
counter2 = counter(20)

print(counter1())
print(counter2())
print(counter1())
print(counter2())
print(counter1())
print(counter2())