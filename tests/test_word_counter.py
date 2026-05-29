"""Unit tests for the word counter module."""

import pytest

from word_counter import read_text_file


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
