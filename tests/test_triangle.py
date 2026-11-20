import unittest

from app.triangle import area, perimeter


class TestTriangle(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(4, 3), 6)
        self.assertEqual(area(5, 2.5), 6.25)

    def test_perimeter(self):
        self.assertEqual(perimeter(3, 4, 5), 12)
        self.assertEqual(perimeter(2.5, 2.5, 3), 8)

    def test_zero_height(self):
        self.assertEqual(area(5, 0), 0)

    def test_area_negative_value(self):
        with self.assertRaises(ValueError):
            area(-4, 3)

    def test_perimeter_negative_value(self):
        with self.assertRaises(ValueError):
            perimeter(-3, 4, 5)

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            area(None, 3)
        with self.assertRaises(TypeError):
            perimeter(None, 4, 5)

    def test_string_type(self):
        with self.assertRaises(TypeError):
            area("4", 3)
        with self.assertRaises(TypeError):
            perimeter("3", 4, 5)


if __name__ == "__main__":
    unittest.main()
