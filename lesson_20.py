"""
19.01.2025
Тема: ООП Ч5. Наследование. Множественное. Иерархическое. MRO. Урок: 20
- Взаимозависимость классов
- Вызов метода наследника через родителя
- Пример иерархического наследования с вызовом инициализаторов предков и передачей атрибутов
- Пример иерархического наследования с вызовом инициализаторов предков и передачей атрибутов через словарь и **kwargs
- Множественное наследование
- MRO - method resolution order - порядок разрешения методов
- Mixin -
"""


class SwimMixin:
    def swim(self):
        return f"{self.__class__.__name__} по имени {self.name} плавает по воде"

class FlyMixin:
    def fly(self):
        return f"{self.__class__.__name__} по имени {self.name} летает в небе"

class RunMixin:    
    def run(self):
        return f"{self.__class__.__name__} по имени {self.name} бегает по земле"


# Базовый класс животного
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} кушает"


class Duck(Animal, SwimMixin, FlyMixin):
    def make_sound(self):
        return "Кря-кря"


class Cat(Animal, RunMixin):
    def make_sound(self):
        return "Мяу"


class Penguin(Animal, SwimMixin, RunMixin):
    def make_sound(self):
        return "Хонк-хонк"


scrooge = Duck("Скрудж")
tom = Cat("Том")
skipper = Penguin("Шкипер")

print(scrooge.swim())
print(scrooge.fly())
print(tom.run())
print(skipper.swim())
print(skipper.run())
