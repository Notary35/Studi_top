"""
Тема: ООП Ч10. Знакомство с патернами. Урок 29
- Одиночка (Singleton)
"""

class SingleTone:
    _instances = None
    def __new__(cls):
        if cls._instances is None:
            cls._instances = super().__new__(cls)
        return cls._instances

    def __str__(self) -> str:
        return f"Экземпляр класса Singletone id: {id(self)}"


if __name__ == "__main__":
    first = SingleTone()
    second = SingleTone()

    print(first)
    print(second)