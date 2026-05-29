"""Утиліти та CLI для пошуку найпопулярніших слів у текстовому файлі."""

import argparse
from collections import Counter
import re


def read_text_file(file_path):
    """Зчитати та повернути текст із .txt файлу."""
    if not str(file_path).lower().endswith(".txt"):
        raise ValueError("Вхідний файл повинен мати розширення .txt.")

    with open(file_path, "r", encoding="utf-8") as text_file:
        return text_file.read()


def extract_words(text):
    """Повернути нормалізовані слова з тексту."""
    return re.findall(r"[^\W\d_]+(?:['’-][^\W\d_]+)?", text.lower())


def get_top_words(words, limit=10):
    """Повернути найпопулярніші слова та кількість їх повторень."""
    return Counter(words).most_common(limit)


def write_word_counts(file_path, word_counts):
    """Записати кількість слів у файл у форматі слово-кількість."""
    with open(file_path, "w", encoding="utf-8") as result_file:
        for word, count in word_counts:
            result_file.write(f"{word}-{count}\n")


def process_text_file(input_path, output_path, limit=10):
    """Обробити текстовий файл і зберегти найпопулярніші слова."""
    text = read_text_file(input_path)
    words = extract_words(text)
    top_words = get_top_words(words, limit)
    write_word_counts(output_path, top_words)
    return top_words


def main(args=None):
    """Запустити інтерфейс командного рядка."""
    parser = argparse.ArgumentParser(
        description="Знайти найпопулярніші слова у .txt файлі."
    )
    parser.add_argument("input_file", help="Шлях до вхідного .txt файлу.")
    parser.add_argument("output_file", help="Шлях до файлу з результатом.")
    parser.add_argument(
        "--limit",
        type=int,
        default=10,
        help="Кількість найпопулярніших слів для збереження.",
    )
    parsed_args = parser.parse_args(args)

    process_text_file(
        parsed_args.input_file,
        parsed_args.output_file,
        parsed_args.limit,
    )


if __name__ == "__main__":
    main()
