from app import _validate_dimensions


def area(a: int | float) -> int | float:
    """Возвращает площадь квадрата."""
    _validate_dimensions(a)
    return a * a


def perimeter(a: int | float) -> int | float:
    """Возвращает периметр квадрата."""
    _validate_dimensions(a)
    return 4 * a
