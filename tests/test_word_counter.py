"""Unit tests for the word counter module."""

import pytest

from word_counter import (
    extract_words,
    get_top_words,
    main,
    process_text_file,
    read_text_file,
    write_word_counts,
)


@pytest.fixture
def sample_text_file(tmp_path):
    file_path = tmp_path / "sample.txt"
    file_path.write_text(
        "Python is simple. Python is powerful.",
        encoding="utf-8",
    )
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
        (
            "Привіт, світ! Привіт.",
            ["привіт", "світ", "привіт"],
        ),
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


def test_write_word_counts_creates_result_file(tmp_path):
    result_file = tmp_path / "result.txt"
    write_word_counts(result_file, [("python", 3), ("test", 2)])

    assert result_file.read_text(encoding="utf-8") == "python-3\ntest-2\n"


def test_process_text_file_saves_top_words(tmp_path):
    input_file = tmp_path / "input.txt"
    output_file = tmp_path / "output.txt"
    input_file.write_text(
        "Python test python code. Code review test python.",
        encoding="utf-8",
    )

    result = process_text_file(input_file, output_file, limit=2)

    assert result == [("python", 3), ("test", 2)]
    assert output_file.read_text(encoding="utf-8") == "python-3\ntest-2\n"


def test_main_processes_file_from_arguments(tmp_path):
    input_file = tmp_path / "input.txt"
    output_file = tmp_path / "output.txt"
    input_file.write_text("one two two three three three", encoding="utf-8")

    main([str(input_file), str(output_file), "--limit", "2"])

    assert output_file.read_text(encoding="utf-8") == "three-3\ntwo-2\n"
