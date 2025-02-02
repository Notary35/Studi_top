"""
Lesson 19
18.01.2025
Тема: ООП Ч4. Наследование. Abstractmethod. Super. Переопределение и расширение. Урок: 19
- Базовый пример на следования
- переопределение метода voice в наследнике
- Проверка доступа защищенных и приватных атрибутов в наследнике (защищенные доступны, приватные нет)
- Отвлеклись на Дебаггер
- Цепочка наследования классов
- Цепочка наследования классов с применением **kwargs
"""

# Создаём миксины для различных способностей животных


class SwimMixin:
    def swim(self):
        return f"{self.__class__.__name__} плавает в воде"


class FlyMixin:
    def fly(self):
        return f"{self.__class__.__name__} летит по небу"


class RunMixin:
    def run(self):
        return f"{self.__class__.__name__} бежит по земле"


# Базовый класс животного


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} кушает"


# Теперь создаём конкретных животных с нужными способностями


class Duck(Animal, SwimMixin, FlyMixin):
    def make_sound(self):
        return "Кря-кря!"


class Cat(Animal, RunMixin):
    def make_sound(self):
        return "Мяу!"


class Penguin(Animal, SwimMixin, RunMixin):
    def make_sound(self):
        return "Ква-ква!"


# Создаём животных

donald = Duck(name="Дональд")
murzik = Cat(name="Мурзик")
rico = Penguin(name="Рико")

# Проверяем их способности

print(donald.swim())  # Выведет: Duck плавает в воде
print(donald.fly())  # Выведет: Duck летит по небу
print(murzik.run())  # Выведет: Cat бежит по земле
print(rico.swim())  # Выведет: Penguin плавает в воде
