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
"""


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
            f"Продолжительность: {self.duration}"
        )


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
composition2 = MusicComposition(name="Дежавю", author="kizaru", year=2019, duration=174)

playlist = PlayList(name="Дежавю")

playlist += composition1
playlist = playlist + composition2
print(playlist)
