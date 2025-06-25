"""
Тема: ООП Ч11. Порождающие патерны. Практика. Урок 30
- Строитель (Builder)
"""

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Pizza:
    available_products = [
        "сыр",
        "грибы",
        "колбаса",
        "оливки",
        "перец",
        "томаты",
        "анчоусы",
        "лосось",
    ]
    available_sizes = ["Маленькая", "Средняя", "Большая", ""]
    size: str
    cheese_bord: bool
    additional_ingredients: List[str]

    def __post_init__(self):
        if any(
            ingredient.lower() not in self.available_products
            for ingredient in self.additional_ingredients
        ):
            raise ValueError("Недопустимые ингредиенты")

        if self.size.capitalize() not in self.available_sizes:
            raise ValueError("Недопустимые размеры")

    def __str__(self):
        return f"Пицца, Размер: {self.size}, Сырный борт: {self.cheese_bord}, Дополнительные ингредиенты: {self.additional_ingredients}"


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza(size="", cheese_bord=False, additional_ingredients=[])

    def set_size(self, size):
        self.pizza.size = size
        return self

    def add_cheese_bord(self):
        self.pizza.cheese_bord = True
        return self

    def add_ingredients(self, *ingredients):
        self.pizza.additional_ingredients.extend(list(ingredients))
        return self

    def build(self):
        return self.pizza


class PizzaManager:
    def __init__(self):
        self.builder = PizzaBuilder()

    def make_pizza(self, size, cheese_bord, *ingredients):
        self.pizza = self.builder.set_size(size).add_ingredients(*ingredients).build()

        if cheese_bord:
            self.pizza = self.builder.add_cheese_bord().build()
        return self.pizza


if __name__ == "__main__":
    manager = PizzaManager()
    pizza = manager.make_pizza("Большая", True, "колбаса", "оливки", "томаты")
    print(pizza)
