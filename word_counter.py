"""Utilities and CLI for finding the most common words in a text file."""

import argparse
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


def process_text_file(input_path, output_path, limit=10):
    """Process a text file and save the most common words."""
    text = read_text_file(input_path)
    words = extract_words(text)
    top_words = get_top_words(words, limit)
    write_word_counts(output_path, top_words)
    return top_words


def main(args=None):
    """Run the command-line interface."""
    parser = argparse.ArgumentParser(
        description="Find the most common words in a .txt file."
    )
    parser.add_argument("input_file", help="Path to the source .txt file.")
    parser.add_argument("output_file", help="Path for the result file.")
    parser.add_argument(
        "--limit",
        type=int,
        default=10,
        help="Number of the most common words to save.",
    )
    parsed_args = parser.parse_args(args)

    process_text_file(
        parsed_args.input_file,
        parsed_args.output_file,
        parsed_args.limit,
    )


if __name__ == "__main__":
    main()
