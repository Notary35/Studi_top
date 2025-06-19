"""
Тема: ООП. Итераторы. Урок: 28
- Пратика с итератором транскриптора

Мы будем работать с результатом работы локальной модели Wisper
Которая транскрибирует речь в текст.

На выходе мы получаем json файл формата

[
    {
        "timestamp": [
            0.0,
            4.62
        ],
        "text": " добро утра здравствуйте"
    },
    ...
]

Нашей задачей будет создать датакласс представляющий собой часть транскрипции и итератор для перебора всех частей транскрипции.

1. Скачать данные
2. Создать экземпляр датакласса с нужными данными
3. Отдать его данные через __next__

TranscriptionChunk:
    text: str
    int_start: int # Начало в секундах
    int_end: int # Конец в секундах
    str_start: str # Начало в формате HH:MM:SS
    str_end: str # Конец в формате HH:MM:SS
"""

from dataclasses import dataclass, field
import json
from typing import Iterator, List, Dict, Optional

JSON_DATA = "lesson_27_ts.json"

@dataclass
class TranscriptionChunk:
    text: str
    float_start: float
    float_end: float
    str_start: str = field(init=False)
    str_end: str = field(init=False)

    def __post_init__(self):
        self.str_start = self._int_to_str(self.float_start)
        self.str_end = self._int_to_str(self.float_end)

    def _int_to_str(self, time: float) -> str:
        int_time = int(time)
        hours = (int_time // 3600)
        minutes = ((int_time % 3600) // 60)
        seconds = (int_time % 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


class TranscriptionIterator:

    ITERATIONS_MODES = {
        "simple": "_simple_iteration",
        "text_length": "_text_length_iteration"
    }
    def __init__(self, transcription_data: List[Dict[str, List[Optional[float]]|str]]):
        self.transcription_data = transcription_data
        self.index = 0
        self.data_len = len(self.transcription_data)
        self._iter_method = self._simple_iteration
        self._chars = 0

    def __iter__(self) -> Iterator[TranscriptionChunk]:
        return self
    
    
    def __next__(self) -> TranscriptionChunk:
        if self._iter_method == self._simple_iteration:
            return self._simple_iteration()
        return self._text_length_iteration(self._chars)
    
    def _simple_iteration(self) -> TranscriptionChunk:
        if self.index >= self.data_len:
            raise StopIteration
        data = self.transcription_data[self.index]
        self.index += 1
        return self._chunk_serialize(data)
    
    def _text_length_iteration(self, chars: int) -> TranscriptionChunk:
        """
        Метод, который будет возвращать куски длинной chars символов
        А так же таймкоды (стартовый первой части и финишный последней части)
        """
        data = self.transcription_data[self.index]
        start_timestamp = data['timestamp'][0]
        end_timestamp = 0
        current_chars = 0
        text = ''
        while current_chars < chars:
            text += data['text']
            current_chars += len(data['text'])
            end_timestamp = data['timestamp'][1] if data['timestamp'][1] is not None else start_timestamp
            self.index += 1
            if self.index >= self.data_len:
                break
            data = self.transcription_data[self.index]
        
        instance = TranscriptionChunk(text, start_timestamp, end_timestamp)
        return instance

    def set_iteration_mode(self, mode: str = "simple", chars: int|None = None) -> None:
        """
        Метод для установки режима итерации
        :param mode: Режим итерации
        :param chars: Количество символов для итерации
        :raise ValueError: Если режим итерации не поддерживается
        """
        if mode not in self.ITERATIONS_MODES:
            raise ValueError(f"Режим итерации {mode} не поддерживается")
        
        mode_method = getattr(self, self.ITERATIONS_MODES[mode])
        
        if mode == "text_length":
            if chars is None:
                raise ValueError("Параметр chars должен быть задан")
            self._chars = chars
        
        self._iter_method = mode_method
        
    def _chunk_serialize(self, data: Dict[str, List[Optional[float]]|str]) -> TranscriptionChunk:
        text = data["text"]
        start = data["timestamp"][0]
        end = data["timestamp"][1] if data["timestamp"][1] is not None else start + 1
        
        instance = TranscriptionChunk(text, start, end)
        return instance

def main():
    with open(JSON_DATA, "r", encoding="utf-8") as file:
        data = json.load(file)
    iterator = TranscriptionIterator(data)
    iterator.set_iteration_mode("text_length", 200)
    
    for i in range(5):
        print(next(iterator))
        
        
if __name__ == "__main__":
    main()