# Top Words Counter

Python script for reading a `.txt` file, finding the 10 most common words,
and saving the result to a new file in `word-count` format.

## Install dependencies

```bash
pip install -r requirements.txt
```

## Run the script

```bash
python word_counter.py input.txt output.txt
```

To change the number of words:

```bash
python word_counter.py input.txt output.txt --limit 10
```

## Run tests and generate HTML report

```bash
pytest --html=report.html --self-contained-html
```

## Check PEP8

```bash
flake8 .
```
