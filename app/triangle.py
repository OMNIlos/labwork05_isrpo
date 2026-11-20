from app import _validate_dimensions


def area(a: int | float, h: int | float) -> float:
    """Возвращает площадь треугольника по основанию и высоте."""
    _validate_dimensions(a, h)
    return a * h / 2


def perimeter(a: int | float, b: int | float, c: int | float) -> int | float:
    """Возвращает периметр треугольника."""
    _validate_dimensions(a, b, c)
    return a + b + c
