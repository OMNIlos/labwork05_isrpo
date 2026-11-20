# Lab work 05 — CI/CD

GitHub Actions запускает модульные тесты проекта на каждом `push`.

## Локальная проверка

Требуется Python 3.11 или новее. Проект использует только стандартные библиотеки Python.

```bash
python -m unittest discover -s tests -v
```

## CI

Workflow находится в `.github/workflows/main.yml`. Матрица запускает одинаковые тесты на `ubuntu-latest` и `windows-latest`.
