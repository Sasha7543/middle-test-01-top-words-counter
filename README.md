# Лічильник найпопулярніших слів

Python-скрипт зчитує файл із розширенням `.txt`, знаходить 10
найпопулярніших слів у тексті та записує результат у новий файл у форматі
`слово-кількість`.

## Встановлення залежностей

```bash
python -m pip install -r requirements.txt
```

## Приклад запуску скрипта

Спочатку створіть файл `input.txt` із текстом. Наприклад:

```bash
echo "кіт пес кіт школа школа школа python python python python" > input.txt
```

Потім запустіть скрипт:

```bash
python word_counter.py input.txt output.txt
```

Результат буде записано у файл `output.txt` у форматі `слово-кількість`.

Приклад результату:

```text
python-4
школа-3
кіт-2
пес-1
```

Щоб змінити кількість слів у результаті:

```bash
python word_counter.py input.txt output.txt --limit 10
```

## Запуск тестів

```bash
python -m pytest tests
```

## Створення HTML-звіту pytest-html

```bash
python -m pytest --html=report.html --self-contained-html
```

Після виконання команди звіт буде доступний у файлі `report.html`.

## Перевірка відповідності PEP8

```bash
python -m flake8 .
```

## Continuous Integration

У репозиторії налаштовано GitHub Actions. Після кожного `push` автоматично
запускаються unit-тести та перевірка коду на відповідність PEP8.
