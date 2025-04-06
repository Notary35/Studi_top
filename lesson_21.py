"""
25.01.2025
Тема: ООП Ч4. Разбор ДЗ. Магические методы. Урок 21.
- Разбор ДЗ с Наследованием и абстрактным классом Файл
- Повторение миксинов
- Магические методы:
    - __init__ - инициализация объекта
    - __str__ - метод, который возвращает строку с описанием объекта
    - __repr__ - тоже описание объекта. Либо техническое, либо строка для создания объекта
    - __len__ - метод, который возвращает длину объекта
    - __call__ - метод, который позволяет вызывать объект как функцию
    - __bool__ - метод, который позволяет преобразовать объект в булево значение
"""

class Duck:
    default_status = "alive"
    
    def __init__(self, name: str, weight: float):
        self.name = name
        self.status = self.default_status
        self.weight = weight
        
    def __str__(self):
        return f"Утка: {self.name} - {self.status}"
    
    def __call__(self, cooking_type: str):
        self.status = cooking_type
        # print(f"Утка {self.name} готовится к {cooking_type}")
    
    def __len__(self):
        return round(self.weight)
    
    def __bool__(self):
        return self.status != self.default_status

# Создаем уток
duck1 = Duck("Donald", 3.5)
duck2 = Duck("Daisy", 4.8)
ducks = [duck1, duck2]

# Выводим информацию об утках
print("\n".join(str(duck) for duck in ducks))
print(f"\nВес уток: {len(duck1)}, {len(duck2)}")

# Сортируем и выводим уток по весу
sorted_ducks = sorted(ducks, key=len)
print("\nОтсортированные утки:")
print("\n".join(str(duck) for duck in sorted_ducks))

duck1("Пожарена")

if duck2:
    print("Утка готова.", duck2.status)
else:
    print("Утка не готова.", duck2.status)