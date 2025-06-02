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


def cach_sorter() -> Callable[[list[str]], list[str]]:
    cach = []
    last_input = []
    def sorter(data: list[str]) -> list[str]:
        nonlocal cach, last_input
        if data != last_input:
            print("Выполняется сортировка")
            cach = sorted(data)
            last_input = data.copy()
            return cach
        print("Выполняется кэш")
        return cach
    return sorter

sorter = cach_sorter()
shop_list = ["Айфон", "Айпад", "Макбук", "Пирожок"]

print(sorter(shop_list))
shop_list.append("PS5")
print(sorter(shop_list))