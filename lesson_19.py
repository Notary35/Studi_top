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
        print("Инициализатор родителя\n")
        
    def __str__(self):
        return f"Животное: {self._name}"
        
    def voice(self) -> None:
        print(f"Животное издаёт звук: {self.sound}")
        

        

class Dog(Animal):
    def voice(self) -> None:
        print(f"Собака {self._name} говорит: {self.sound}")
    # pass

dog = Dog('Шарик', 'Гав - гав')
# print(isinstance(dog, Animal))
print(dog)
# <__main__.Dog object at 0x000001D8B5276A50>
print()
print(type(dog))
# <class '__main__.Dog'>
print()
dog.voice()
print()