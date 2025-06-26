"""
Тема: ООП Ч11. Порождающие паттерны. Практика. Урок: 30
- Строитель (Builder)
- Абстрактная фабрика (Abstract Factory)
"""

"""
Полная версия.
Абстрактная фабрика (Abstract Factory)

Структура классов
- АБСТРАКТНЫЕ ПРОДУКТЫ
    - AbstractImageAnalyzer
    - AbstractTextGenerator
    - AbstractTextFormatter
    - AbstractAudioTrascriber

- АБСТРАКТНАЯ ФАБРИКА
    - AbstractProductFactory

- Реальные продукты
    - ClaudeImageAnalyzer
    - ClaudeTextGenerator


    - OpenAiAudioTranscriber
    - OpenAiImageAnalyzer
    - OpenAiTextGenerator

    - MistralImageAnalyzer
    - MistralTextGenerator
"""

from typing import List, Optional
from abc import ABC, abstractmethod

class AbstractImageAnalyzer(ABC):
    @abstractmethod
    def analyze_image(self, image_path: str):
        pass

class AbstractTextGenerator(ABC):
    @abstractmethod
    def generate_text(self, prompt: str):
        pass


class OpenAiImageAnalyzer(AbstractImageAnalyzer):
    def analyze_image(self, image_path: str):
        print(f'OpenAI: Анализ изображения {image_path}')
        return f'OpenAI: Результат анализа {image_path}'


class OpenAiTextGenerator(AbstractTextGenerator):
    def generate_text(self, prompt: str):
        print(f'OpenAI: Генерация текста на основе {prompt}')
        return f'OpenAI: Результат генерации текста {prompt}'


class MistralImageAnalyzer(AbstractImageAnalyzer):
    def analyze_image(self, image_path: str):
        print(f'Mistral: Анализ изображения {image_path}')
        return f'Mistral: Результат анализа {image_path}'


class MistralTextGenerator(AbstractTextGenerator):
    def generate_text(self, prompt: str):
        print(f'Mistral: Генерация текста на основе {prompt}')
        return f'Mistral: Результат генерации текста {prompt}'


# Абстрактная фабрика

class AbstractProductFactory(ABC):
    @abstractmethod
    def create_image_analyzer(self) -> AbstractImageAnalyzer:
        pass

    @abstractmethod
    def create_text_generator(self) -> AbstractTextGenerator:
        pass


# Реальные продукты

class OpenAiFactory(AbstractProductFactory):
    def create_image_analyzer(self) -> AbstractImageAnalyzer:
        return OpenAiImageAnalyzer()

    def create_text_generator(self) -> AbstractTextGenerator:
        return OpenAiTextGenerator()


class MistralFactory(AbstractProductFactory):
    def create_image_analyzer(self) -> AbstractImageAnalyzer:
        return MistralImageAnalyzer()

    def create_text_generator(self) -> AbstractTextGenerator:
        return MistralTextGenerator()

# Сделаем анализ картинки с помощью OpenAI
if __name__ == '__main__':
    openai_factory = OpenAiFactory()
    openai_image_analyzer = openai_factory.create_image_analyzer()
    
    image_path = input('Введите путь к изображению: ')
    openai_image_analyzer.analyze_image(image_path)
    