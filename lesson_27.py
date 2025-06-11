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

MIN_VALUE = 0
MAX_VALUE = 1000
my_range = list(range(MIN_VALUE, MAX_VALUE + 1))

# обработка через filter()
even_nums = filter(lambda num: num % 2 == 0, my_range)

# обработка через map()
strings = map(lambda num: str(num) + " число", even_nums)

# pprint(list(strings))
# pprint(list(map(lambda num: str(num) + " число", filter(lambda num: num % 2 == 0, range(MIN_VALUE, MAX_VALUE + 1)))))

for num in strings:
    print(num)
    sleep(0.01)


