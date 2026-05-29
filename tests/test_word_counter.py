"""Unit tests for the word counter module."""

import pytest

from word_counter import extract_words, get_top_words, read_text_file


@pytest.fixture
def sample_text_file(tmp_path):
    file_path = tmp_path / "sample.txt"
    file_path.write_text("Python is simple. Python is powerful.", encoding="utf-8")
    return file_path


def test_read_text_file_returns_content(sample_text_file):
    assert read_text_file(sample_text_file) == (
        "Python is simple. Python is powerful."
    )


def test_read_text_file_rejects_non_txt_file(tmp_path):
    file_path = tmp_path / "sample.md"
    file_path.write_text("Wrong extension", encoding="utf-8")

    with pytest.raises(ValueError, match=".txt"):
        read_text_file(file_path)


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Hello, hello! WORLD.", ["hello", "hello", "world"]),
        ("Python 3.12 is cool", ["python", "is", "cool"]),
        ("Привіт, світ! Привіт.", ["привіт", "світ", "привіт"]),
        ("don't stop", ["don't", "stop"]),
    ],
)
def test_extract_words_returns_normalized_words(text, expected):
    assert extract_words(text) == expected


@pytest.mark.parametrize(
    ("words", "limit", "expected"),
    [
        (["a", "b", "a", "c", "b", "a"], 10, [("a", 3), ("b", 2), ("c", 1)]),
        (["one", "two", "one", "three"], 2, [("one", 2), ("two", 1)]),
        ([], 10, []),
    ],
)
def test_get_top_words_returns_limited_counts(words, limit, expected):
    assert get_top_words(words, limit) == expected
