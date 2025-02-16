"""
Тема: ООП. Итераторы. Урок: 28
- Практика с итератором транскрипции

Мы будем работать с результатом работы локальной модели Wisper
Которая транскрибирует речь в текст.

На выходе мы получаем json файл формата

[
    {
        "timestamp": [
            0.0,
            4.62
        ],
        "text": " добро утра здравствуйте"
    },
    ...
]

Нашей задачей будет создать датакласс представляющий собой часть транскрибации и итератор
для перебора всех частей транскрибации.

1. Считать данные
2. Создать экземпляр датакласса с нужными данными
3. Отдать его дальше через __next__
"""

from dataclasses import dataclass, field
import json
from typing import Iterator, List, Dict


@dataclass
class TranscriptionChunk:
    text: str
    float_start: float
    float_end: float
    str_start: str = field(init=False)
    str_end: str = field(init=False)

    def __post_init__(self):
        self.str_start = self.float_start
        self.str_end = self.float_end

    def _int_to_str(self, time: float) -> str:
        int_time = int(time)
        hours = int_time // 3600
        minutes = (int_time % 3600) // 60
        seconds = int_time % 60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def main():
    test_data = {"timestamp": [0.0, 4.62], "text": "добро утра здравствуйте"}

    transcription_chunks = TranscriptionChunk(
        test_data["text"], test_data["timestamp"][0], test_data["timestamp"][1]
    )
    print(transcription_chunks)


if __name__ == "__main__":
    main()
    exit()
