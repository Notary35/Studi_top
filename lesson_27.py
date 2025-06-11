"""
Тема: Генераторы и Итераторы. Урок: 27
"""
from pprint import pprint
from time import sleep
string = "Бананы"
my_list = ["Банан", "Яблоко", "Апельсин"]

# Служебные объекты генератора Python
# dict.keys()
# dict.values()
# dict.items()
# range()
# enumerate()
# map()
# filter()
# zip()

MIN_VALUE = 1
MAX_VALUE = 100000

my_range = list(range(MIN_VALUE, MAX_VALUE + 1))

# обработка через filter()
even_nums = filter(lambda num: num % 2 == 0, my_range)

# обработка через map()
strings = map(lambda num: str(num) + " число", even_nums)

# pprint(list(strings))
# pprint(list(map(lambda num: str(num) + " число", filter(lambda num: num % 2 == 0, range(MIN_VALUE, MAX_VALUE + 1)))))

Stop_Item = "10000 число"

# with open("nums.txt", "w", encoding="utf-8") as file:
#     for num in strings:
#         if num == Stop_Item:
#             break
#         file.write(num + "\n")

SEARCH_STRING = "9982"

# with open("nums.txt", "r", encoding="utf-8") as file:
#     for num in file:
#         if SEARCH_STRING in num:
#             print(num)
#             break

from typing import Any, Generator

def my_generator(start: int, stop: int) -> Generator[int]:
    for i in range(start, stop):
        yield i

gen = my_generator(0, 2)

print(next(gen))
print(next(gen))
print(next(gen))