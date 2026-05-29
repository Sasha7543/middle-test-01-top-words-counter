# Лічильник найпопулярніших слів

Python-скрипт зчитує файл із розширенням `.txt`, знаходить 10
найпопулярніших слів у тексті та записує результат у новий файл у форматі
`слово-кількість`.

## Встановлення залежностей

```bash
pip install -r requirements.txt
```

## Запуск скрипта

```bash
python word_counter.py input.txt output.txt
```

Щоб змінити кількість слів у результаті:

```bash
python word_counter.py input.txt output.txt --limit 10
```

## Запуск тестів і створення HTML-звіту

```bash
pytest --html=report.html --self-contained-html
```

## Перевірка відповідності PEP8

```bash
flake8 .
```
