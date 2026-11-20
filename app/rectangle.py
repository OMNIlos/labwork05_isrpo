from app import _validate_dimensions


def area(a: int | float, b: int | float) -> int | float:
    """Возвращает площадь прямоугольника."""
    _validate_dimensions(a, b)
    return a * b


def perimeter(a: int | float, b: int | float) -> int | float:
    """Возвращает периметр прямоугольника."""
    _validate_dimensions(a, b)
    return 2 * (a + b)
