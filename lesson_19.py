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
# pylint: disable=all

from abc import ABC, abstractmethod
class AbstracDocument(ABC):
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    @abstractmethod    
    def open(self) -> None:
        pass
    
    @abstractmethod
    def read(self) -> None:
        pass
    
    @abstractmethod
    def append(self) -> None:
        pass
    
    @abstractmethod
    def write(self) -> None:
        pass
    
class MarkdownDocument(AbstracDocument):
    def __init__(self, file_path: str) -> None:
        super().__init__(file_path)
        
    def open(self) -> None:
        pass
    def read(self) -> None:
        pass
    def append(self) -> None:
        pass
    def write(self) -> None:
        pass
        
md_file = MarkdownDocument("file.md")
