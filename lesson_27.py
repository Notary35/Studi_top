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

from random import choice
from typing import Generator

fruit_list = ["Яблоко", "Апельсин", "Банан", "Груша", "Клубника", "Киви", "Мандарин", "Манго", "Персик", "Слива", "Слива"]

class CoctailGenerator:
    def __init__(self, products: list[str]):
        self.products = products

    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.products:
            raise StopIteration
        fruit = choice(self.products)
        self.products.remove(fruit)
        return f"Коктейль из {fruit}"


coctail_gen = CoctailGenerator(fruit_list)

for coctail in coctail_gen:
    print(coctail)  