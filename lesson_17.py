"""
Lesson 17
11.05.2025
Инкапсуляция. Приватные атрибуты и методы.
"""
# pylint: disable=all

class Car:
    """
    Эксперементальный класс автомобиль
    для изучения приватных и защищённых методов и атрибутов.
    """
    def __init__(self, color: str, mark: str, serial_number: int):
        self.color = color
        self.mark = mark
        self.__serial_number = serial_number
        self.__engine_state: bool = False
    
    def __str__(self):
        # return f"Цвет: {self.color}\nМарка: {self.mark}\nСерийный номер: {self.serial_number}"
        return f"Автомобиль: {self.mark}\nСерийный номер: {self.__serial_number}\nЦвет: {self.color}"
    
    def __make_noise(self):
        print(f"Звук работы двигателя {self.mark}")

    def start_engine(self):
        self.__engine_state = True
        self.__make_noise()
        print(f'Состояние двигателя: {self.__engine_state}')
        
    def stop_engine(self):
        self.__engine_state = False
        print(f'Состояние двигателя: {self.__engine_state}')
        
    def move(self):
        if self.__engine_state:
            print("Автомобиль едет")
            self.__make_noise()
        else:
            print("Двигатель не запущен")
        
    def stop(self):
        print("Автомобиль остановился")

    
# Создаём экземпляр класса автомобиля
car = Car('red', 'BMW', 555)

# Попробуем поехать
car.move()

# Запустим двигатель
car.start_engine()

# Поехали
car.move()

# Остановимся
car.stop()

# Заглушим двигатель
car.stop_engine()

# Попробуем издать звук двигателя
# car.__make_noise() # AttributeError: 'Car' object has no attribute '__make_noise'. Did you mean: '_Car__make_noise'?