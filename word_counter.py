"""Utilities and CLI for finding the most common words in a text file."""

from collections import Counter
import re


def read_text_file(file_path):
    """Read and return text from a .txt file."""
    if not str(file_path).lower().endswith(".txt"):
        raise ValueError("Input file must have a .txt extension.")

    with open(file_path, "r", encoding="utf-8") as text_file:
        return text_file.read()


def extract_words(text):
    """Return normalized words from text."""
    return re.findall(r"[^\W\d_]+(?:['’-][^\W\d_]+)?", text.lower())


def get_top_words(words, limit=10):
    """Return the most common words and their counts."""
    return Counter(words).most_common(limit)


def write_word_counts(file_path, word_counts):
    """Write word counts to a file in word-count format."""
    with open(file_path, "w", encoding="utf-8") as result_file:
        for word, count in word_counts:
            result_file.write(f"{word}-{count}\n")


def main():
    """Run the command-line interface."""
    pass


if __name__ == "__main__":
    main()
