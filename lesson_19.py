"""
Lesson 19
12.01.2025
Тема: ООП Ч4. Наследование. Abstractmethod. Super. Переопределение и расширение. Урок: 19
- Базовый пример на следования
- переопределение метода voice в наследнике
- Проверка доступа защищенных и приватных атрибутов в наследнике (защищенные доступны, приватные нет)
- Отвлеклись на Дебаггер
- Цепочка наследования классов
- Цепочка наследования классов с применением **kwargs
"""
class Animal:
    def __init__ (self, name: str, sound: str):
        self._name = name
        self.sound = sound
        print("Инициализатор родительского класса\n")
        
    def __str__(self):
        return f"Животное: {self._name}\n"
        
    def voice(self) -> None:
        return f"Животное издаёт звук: {self.sound}\n"
        
class Dog(Animal):
    def __init__(self, name: str, sound: str, breed: str):
        # Animal.__init__(self, name, sound)
        super().__init__(name, sound)
        self.breed = breed
        print("Инициализатор дочернего класса\n")
        
        
    def voice(self) -> None:
        # animal_voice = Animal.voice(self)
        animal_voice = super().voice(), "\n"
        animal_voice += "\n"
        return animal_voice
    # pass

dog = Dog('Шарик', 'Гав-гав', 'Стафф')
# print(isinstance(dog, Animal))
print(dog)
# <__main__.Dog object at 0x000001D8B5276A50>

print(type(dog))
print()
# <class '__main__.Dog'>

print(dog.voice())
