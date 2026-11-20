import math

from app import _validate_dimensions


def area(r: int | float) -> float:
    """Возвращает площадь круга по радиусу."""
    _validate_dimensions(r)
    return math.pi * r * r


def perimeter(r: int | float) -> float:
    """Возвращает длину окружности по радиусу."""
    _validate_dimensions(r)
    return 2 * math.pi * r
