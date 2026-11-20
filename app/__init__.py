"""Функции для вычисления площади и периметра фигур."""


def _validate_dimensions(*values: int | float) -> None:
    """Проверяет, что размеры являются неотрицательными числами."""
    for value in values:
        if type(value) not in (int, float):
            raise TypeError("Размер должен быть числом")
        if value < 0:
            raise ValueError("Размер не может быть отрицательным")
