"""Utilities and CLI for finding the most common words in a text file."""


def read_text_file(file_path):
    """Read and return text from a .txt file."""
    if not str(file_path).lower().endswith(".txt"):
        raise ValueError("Input file must have a .txt extension.")

    with open(file_path, "r", encoding="utf-8") as text_file:
        return text_file.read()


def main():
    """Run the command-line interface."""
    pass


if __name__ == "__main__":
    main()
