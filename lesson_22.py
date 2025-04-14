"""
26.01.25
Тема: ООП Ч7. Магические методы. Математика. Сравнение. Знакомство с Dataclasses. Урок 22

- Магические методы математика:
- __add__ - сложение
- __sub__ - вычитание
- __mul__ - умножение
- __truediv__ - деление
- __floordiv__ - целочисленное деление
- __mod__ - остаток от деления
- __pow__ - возведение в степень
- __abs__ - модуль числа
- __round__ - округление числа
- __ceil__ - округление вверх
- __floor__ - округление вниз
- __int__ - преобразование в целое число
- __float__ - преобразование в число с плавающей точкой


Инплейс операции

- __iadd__ - +=
- __isub__ - -=
- __imul__ - *=
- __itruediv__ - /=
- __ifloordiv__ - //=

- __str__ - метод, который возвращает строку с описанием объекта
- __repr__ - тоже описание объекта. Либо техническое, либо строка для создания объекта

Сравнение объектов

- less then - __lt__ - меньше <
- greater then - __gt__ - больше >
- less or equal - __le__ - меньше или равно <=
- greater or equal - __ge__ - больше или равно >=
- equal - __eq__ - равно ==
- not equal - __ne__ - не равно !=

from functools import total_ordering
"""
from pprint import pprint

class MusicComposition:
    def __init__(self, name: str, author: str, year: int, duration: int):
        self.name = name
        self.author = author
        self.year = year
        self.duration = duration
        
    def __str__(self):
        return (
            f"Название: {self.name}\n"
            f"Автор: {self.author}\n"
            f"Год выпуска: {self.year}\n"
            f"Продолжительность: {self.duration} сек."
        )
    
    def __repr__(self):
        return f"MusicComposition('{self.name}', '{self.author}', '{self.year}', '{self.duration}')"

    def __eq__(self, other):
        if not isinstance(other, MusicComposition):
            raise TypeError("Неверный тип данных")
        return (
            self.duration == other.duration
        )

    def __lt__(self, other):
        if not isinstance(other, MusicComposition):
            raise TypeError("Неверный тип данных")
        return self.duration < other.duration

    def __ge__(self, other):
        if not isinstance(other, MusicComposition):
            raise TypeError("Неверный тип данных")
        return self.duration >= other.duration


class PlayList:
    def __init__(self, name):
        self.name = name
        self.tracks: list[MusicComposition] = []

    def __len__(self):
        return len(self.tracks)

    def __str__(self):
        return f"Название плейлиста: {self.name}\n" f"Количество треков: {len(self)}"
        

    def __iadd__(self, other: MusicComposition) -> "PlayList":
        if not isinstance(other, MusicComposition):
            raise TypeError("Неверный тип данных")
        self.tracks.append(other)
        return self

    def __add__(self, other: MusicComposition) -> "PlayList":
        return self.__iadd__(other)


composition1 = MusicComposition(name="Дежавю", author="kizaru", year=2019, duration=174)
composition2 = MusicComposition(name="Money long", author="kizaru", year=2019, duration=124)

# playlist = PlayList(name="Karmageddon")

# playlist += composition1
# playlist = playlist + composition2
# print(playlist)

# composition = [composition1, composition2]
# # print(composition)
# print(f"{composition[0]}\n{composition[1]}")

# # rep = repr(composition[0])
# # obj = eval(rep)
# # rep2 = repr(composition[1])
# # obj2 = eval(rep2)
# # # print(rep)
# # print(obj)
# # print(obj2)

# # Теперь мы можем сравнивать объекты
# print(composition1 == composition2)
# print(composition1 != composition2)
# print(composition1 < composition2)
# print(composition1 > composition2)
# print(composition1 >= composition2)
# print(composition1 <= composition2)


# Датаклассы
from dataclasses import dataclass

@dataclass
class MusicCompositionData:
    name: str
    author: str
    year: int
    duration: int
    
m_data = MusicCompositionData(
    name = "Through The Valley",
    author = "Shawn James",
    year = 2020,
    duration = 245
)

pprint(m_data)